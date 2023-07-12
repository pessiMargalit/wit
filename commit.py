import os
import fileHandler
import wit
import secrets


class Commit:
    commit_id = None

    @classmethod
    def generate_random_hash(cls):
        cls.commit_id = secrets.token_hex(20)

    @classmethod
    def future_access(cls):
        file_path = r".wit\references.txt"
        mode = "a" if os.path.exists(os.path.join(fileHandler.FileHandler.base_path, "references.txt")) else "w"
        with open(file_path, mode) as commit_id_file:
            commit_id_file.write("HEAD={}\n".format(cls.commit_id))
            commit_id_file.write("master={}\n".format(cls.commit_id))

    @classmethod
    def commit(cls, args):
        wit.Wit.add(args)
        commit_id_dir = os.path.join(r'.wit\images', cls.commit_id)
        fileHandler.FileHandler.create_dir(commit_id_dir)
        # path of the commit_id file
        file_path = os.path.join(fileHandler.FileHandler.base_path, fr"images\{cls.commit_id}.txt")
        fileHandler.FileHandler.write_commit_metadata_to_file(file_path, args[1])
        staging_area_path = os.path.join(fileHandler.FileHandler.base_path, "staging_area")
        fileHandler.FileHandler.copy_item(staging_area_path, commit_id_dir)
        Commit.future_access()
