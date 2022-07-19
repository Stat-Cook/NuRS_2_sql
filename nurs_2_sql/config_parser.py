import os
import configparser

from .utils import default_dict


class ConfigParser(configparser.ConfigParser):

    def read(self, filename, encoding=None):
        if not os.path.exists(filename):
            print(f"Config file {filename} not found.  Now writing default version.")
            self.write_config_file(filename)

        return super().read(filename, encoding=encoding)

    def write_config_file(self, filename):

        with open(filename, "w") as f:
            f.write("[DEFAULT]\n")
            for key, value in default_dict.items():
                f.write(f"{key} = {value}\n")
        print(f"Default config file written.  Update values in {filename} and close to continue.")
        return os.system(filename)
