from collections import UserDict

from .config_parser import ConfigParser
from sqlalchemy import engine


class SQLConnection(UserDict):

    @property
    def url_create_args(self):
        return ["drivername", "username", "password", "host", "port", "database"]

    @property
    def con_template(self):
        return "{dialect}://{username}:{password}@{host}:{port}"

    @property
    def connection_string(self):

        create_dict = {i: j for i, j in self.items() if i in self.url_create_args and j}
        query = {i: j for i, j in self.items() if i not in self.url_create_args}

        return engine.URL.create(**create_dict, query=query)


def config_2_con_string(path, config_id="DEFAULT"):
    parser = ConfigParser()
    parser.read(path)

    config = parser[config_id]

    con_string = SQLConnection(**config)

    return con_string.connection_string
