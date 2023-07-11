import sys
import os
import shutil


class FileHandler:
    base_path = None
    working_directory = None

    @staticmethod
    def create_dir(path):
        try:
            os.makedirs(path)
        except:
            raise Exception("Failed to create directory..")

    @classmethod
    def find_base_path(cls):
        if cls.base_path:
            return cls.base_path
        found = False
        if not found:
            raise Exception("Not a wit repository")

    @classmethod
    def validate_path(cls, path):
        full_path = os.path.join(cls.working_directory, path)
        if not os.path.exists(full_path):
            raise FileExistsError("File doesn't exist")
        return full_path

    @classmethod
    def copy_item(cls, origin, target):
        if os.path.isfile(origin):
            shutil.copy(origin, target)
        elif os.path.isdir(origin):
            shutil.copytree(origin, target)
