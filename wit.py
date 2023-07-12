import os
from fileHandler import FileHandler
from commit import Commit


class WitException(Exception):
    pass


class Wit:

    @staticmethod
    def validate_is_wit_repo():
        return FileHandler.find_base_path()

    @staticmethod
    def init():
        if Wit.validate_is_wit_repo():
            raise WitException("Already a wit repository")
        else:
            FileHandler.create_dir(".wit")
            FileHandler.create_dir(".wit/images")
            FileHandler.create_dir(".wit/staging_area")

    @staticmethod
    def move_to_staging(full_path):
        target_path = os.path.join(FileHandler.base_path, "staging_area")
        dirs = full_path[len(FileHandler.base_path)-4::]
        dirs = dirs.split("\\")
        for item in dirs[:-1]:
            target_path = os.path.join(target_path, item)
            if not os.path.exists(target_path):
                os.mkdir(target_path)
        FileHandler.copy_item(full_path, target_path)

    @staticmethod
    def add(args):
        if not Wit.validate_is_wit_repo():
            raise WitException("Not a wit repo")
        full_path = FileHandler.get_full_path(args[0])
        Wit.move_to_staging(full_path)

    @staticmethod
    def commit(args):
        Commit.commit(args)
