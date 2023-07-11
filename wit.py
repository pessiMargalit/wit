import os
import fileHandler


class Wit:

    @staticmethod
    def validate_is_wit_repo():
        return fileHandler.FileHandler.find_base_path()

    @staticmethod
    def init():
        if Wit.validate_is_wit_repo():
            # handle nested wits
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
        full_path = fileHandler.FileHandler.validate_path(args[0])
        Wit.move_to_staging(full_path)

    @staticmethod
    def commit():
        pass
