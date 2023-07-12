import os
from fileHandler import FileHandler
from commit import Commit
from logger import Logger
from costumeException import WitException


class Wit:
    # Logger.logger(file_handler=os.path.join(FileHandler.base_path, "wit_logger.txt"))

    @staticmethod
    def validate_is_wit_repo():
        return FileHandler.find_base_path()

    @staticmethod
    def init():
        try:
            if Wit.validate_is_wit_repo():
                raise WitException("Already a wit repository")
            else:
                Logger.logger.info(f"{__name__}  Init action was activated")
                FileHandler.create_dir(".wit")
                FileHandler.create_dir(".wit/images")
                FileHandler.create_dir(".wit/staging_area")
        except WitException as e:
            Logger.logger.debug(f"{__name__}  {e}")

    @staticmethod
    def move_to_staging(full_path):
        Logger.logger.debug(f"{__name__} in move_to_staging")
        target_path = os.path.join(FileHandler.base_path, "staging_area")
        dirs = full_path[len(FileHandler.base_path) - 4::]
        dirs = dirs.split("\\")
        for item in dirs[:-1]:
            target_path = os.path.join(target_path, item)
            if not os.path.exists(target_path):
                os.mkdir(target_path)
        FileHandler.copy_item(full_path, target_path)

    @staticmethod
    def add(args):
        try:
            if not Wit.validate_is_wit_repo():
                raise WitException("Not a wit repo")
            Logger.logger.info(f"{__name__}  add action was activated with {args[0]} files/folders")
            full_path = FileHandler.get_full_path(args[0])
            Wit.move_to_staging(full_path)
        except WitException as e:
            Logger.logger.debug(f"{__name__} {e}")

    @staticmethod
    def commit(args):
        try:
            Logger.logger.info(f"{__name__}  commit action was activated with message: {args[1]}")
            Commit.commit(args)
        except WitException as e:
            Logger.logger.info(f"{__name__} {e}")
