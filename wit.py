import os
import fileHandler
import secrets
import commit


class Wit:

    @staticmethod
    def validate_is_wit_repo():
        return fileHandler.FileHandler.find_base_path()

    @staticmethod
    def init():
        if Wit.validate_is_wit_repo():
            # raise Exception("The init command has already been done")
            pass
        else:
            fileHandler.FileHandler.create_dir(".wit")
            fileHandler.FileHandler.create_dir(".wit/images")
            fileHandler.FileHandler.create_dir(".wit/staging_area")

    @staticmethod
    def move_to_staging(full_path):
        target_path = os.path.join(fileHandler.FileHandler.base_path, "staging_area")
        fileHandler.FileHandler.copy_item(full_path, target_path)

    @staticmethod
    def add(args):
        Wit.init()
        # if not os.path.exists(fileHandler.FileHandler.base_path):
        #     raise Exception("Sorry....\nInit command is required")
        full_path = fileHandler.FileHandler.validate_path(args[0])
        Wit.move_to_staging(full_path)

    @staticmethod
    def generate_random_hash():
        random_string = secrets.token_hex(20)
        return random_string

    @staticmethod
    def future_access(commit_id):
        file_path = r".wit\references.txt"
        mode = "a" if os.path.exists(os.path.join(fileHandler.FileHandler.base_path, "references.txt")) else "w"
        with open(file_path, mode) as commit_id_file:
            commit_id_file.write("HEAD={}\n".format(commit_id))
            commit_id_file.write("master={}\n".format(commit_id))

    @staticmethod
    def commit(args):
        Wit.add(args)
        commit_id = Wit.generate_random_hash()
        commit_id_dir = os.path.join(r'.wit\images', commit_id)
        fileHandler.FileHandler.create_dir(commit_id_dir)
        # path of the commit_id file
        file_path = os.path.join(fileHandler.FileHandler.base_path, fr"images\{commit_id}.txt")
        fileHandler.FileHandler.write_commit_metadata_to_file(file_path, args[1])
        staging_area_path = os.path.join(fileHandler.FileHandler.base_path, "staging_area")
        fileHandler.FileHandler.copy_item(staging_area_path, commit_id_dir)
        Wit.future_access(commit_id)

    # @staticmethod
    # def commit(args):
    #     commit.Commit.commit(args)
