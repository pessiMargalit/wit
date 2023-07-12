import os
from fileHandler import FileHandler
from commit import Commit


class Wit:

    @staticmethod
    def validate_is_wit_repo():
        return FileHandler.find_base_path()

    @staticmethod
    def init():
        if Wit.validate_is_wit_repo():
            # raise Exception("The init command has already been done")
            pass
        else:
            FileHandler.create_dir(".wit")
            FileHandler.create_dir(".wit/images")
            FileHandler.create_dir(".wit/staging_area")

    @staticmethod
    def move_to_staging(full_path):
        target_path = os.path.join(FileHandler.base_path, "staging_area")
        FileHandler.copy_item(full_path, target_path)

    @staticmethod
    def add(args):
        # Wit.init()
        # if not os.path.exists(FileHandler.base_path):
        #     raise Exception("Sorry....\nInit command is required")
        full_path = FileHandler.validate_path(args[0])
        Wit.move_to_staging(full_path)

    @staticmethod
    def commit(args):
        Commit.commit(args)
