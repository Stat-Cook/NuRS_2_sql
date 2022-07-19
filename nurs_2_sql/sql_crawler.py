from sqlalchemy import create_engine

from .sql_connection import config_2_con_string
from .file_handler import FileHandler
from .crawler import crawler


def sql_crawler(path: str = ".",
                conf_file: str = "conf.ini",
                config_id="DEFAULT",
                db: str = "dev",
                ):
    con_string = config_2_con_string(conf_file, config_id)
    print(con_string)
    engine = create_engine(con_string)

    def to_sql(root, dirs, files):
        data_files = [i for i in files if (i.endswith(".csv") or i.endswith(".tsv"))]
        for file in data_files:
            file_handler = FileHandler(file, root, db)
            file_handler.to_sql(engine)
            print(f"{db}.{file} created")

    crawler(path, to_sql)
