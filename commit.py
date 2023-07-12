import os
from fileHandler import FileHandler
from wit import Wit
import secrets


class Commit:
    commit_id = None

    @classmethod
    def generate_random_hash(cls):
        cls.commit_id = secrets.token_hex(20)

    @classmethod
    def future_access(cls):
        file_path = r".wit\references.txt"
        mode = "a" if os.path.exists(os.path.join(FileHandler.base_path, "references.txt")) else "w"
        with open(file_path, mode) as commit_id_file:
            commit_id_file.write("HEAD={}\n".format(cls.commit_id))
            commit_id_file.write("master={}\n".format(cls.commit_id))

    @classmethod
    def commit_again(cls):
        pass

    @classmethod
    def commit(cls, args):
        Wit.add(args)
        Commit.generate_random_hash()
        commit_id_dir_path = os.path.join(r'.wit\images', cls.commit_id)
        FileHandler.create_dir(commit_id_dir_path)
        # path of the commit_id file
        file_path = os.path.join(FileHandler.base_path, fr"images\{cls.commit_id}.txt")
        FileHandler.write_to_file(file_path, args[1])
        staging_area_path = os.path.join(FileHandler.base_path, "staging_area")
        FileHandler.copy_item(staging_area_path, commit_id_dir_path)
        Commit.future_access()
