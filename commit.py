import os
from fileHandler import FileHandler
import wit
from costumeException import IllegalArgumentError
from logger import Logger
# Imported to use a function to generate a commit_id by a hash function
import secrets


class Commit:
    commit_id = None

    @classmethod
    def generate_random_hash(cls):
        cls.commit_id = secrets.token_hex(20)

    @classmethod
    def write_commit_metadata_to_file(cls, args):
        try:
            commit_metadata_file_path = os.path.join(FileHandler.base_path, fr"images\{cls.commit_id}.txt")
            if not os.path.exists(os.path.join(FileHandler.base_path, "references.txt")):
                FileHandler.write_to_file(commit_metadata_file_path, args[1])
            else:
                parent = Commit.get_prev_commit_id()
                FileHandler.write_to_file(commit_metadata_file_path, args[1], parent=parent)
        except IllegalArgumentError as e:
            Logger.logger.debug(e)

    @staticmethod
    def get_prev_commit_id():
        file_path = r".wit\references.txt"
        with open(file_path, "r") as commit_id_file:
            return commit_id_file.readline()[-41:]

    @classmethod
    def future_access(cls):
        file_path = r".wit\references.txt"
        with open(file_path, "w") as commit_id_file:
            commit_id_file.write("HEAD={}\n".format(cls.commit_id))
            commit_id_file.write("master={}\n".format(cls.commit_id))

    @classmethod
    def commit(cls, args):
        try:
            wit.Wit.add(args)
            Commit.generate_random_hash()
            commit_id_dir_path = os.path.join(r'.wit\images', cls.commit_id)
            FileHandler.create_dir(commit_id_dir_path)
            Commit.write_commit_metadata_to_file(args)
            staging_area_path = os.path.join(FileHandler.base_path, "staging_area")
            FileHandler.copy_item(staging_area_path, commit_id_dir_path)
            Commit.future_access()
        except IllegalArgumentError as e:
            Logger.logger.debug(e)
        except Exception as e:
            Logger.logger.debug(e)
