import sys
import os
import shutil
import datetime


class FileHandler:
    base_path = None
    working_directory = os.getcwd()

    @staticmethod
    def create_dir(path):
        try:
            os.makedirs(path)
        except:
            raise Exception("Failed to create a directory..")

    @classmethod
    def find_base_path(cls):
        if cls.base_path:
            return cls.base_path
        for root, dirs, files in os.walk(cls.working_directory, topdown=False):
            for name in dirs:
                if name == ".wit":
                    cls.base_path = os.path.join(root, name)
                    return cls.base_path

        # TODO: handle not wit repo
        # raise Exception("Not a wit repository")

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
            shutil.copytree(origin, os.path.join(target, origin.split("\\")[-1]))

    @staticmethod
    def write_commit_metadata_to_file(file_path, message):
        with open(file_path, "w") as commit_id_file:
            commit_id_file.write("parent=None\n")
            commit_id_file.write("date={}\n".format(datetime.datetime.now().strftime("%a %b %d %H:%M:%S %Y %z")))
            commit_id_file.write("message={}\n".format(message))


