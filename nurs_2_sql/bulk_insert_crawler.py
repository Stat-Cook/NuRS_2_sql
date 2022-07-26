from sqlalchemy import create_engine

from .sql_connection import config_2_con_string
from .file_handler import FileHandler
from .crawler import crawler


def bulk_insert_crawler(path: str = ".",
                        conf_file: str = "conf.ini",
                        config_id="DEFAULT",
                        db: str = ""):
    con_string = config_2_con_string(conf_file, config_id)
    engine = create_engine(con_string)

    if not db:
        db = None

    def to_sql(root, dirs, files):
        data_files = [i for i in files if (i.endswith(".csv") or i.endswith(".tsv"))]
        for file in data_files:
            file_handler = FileHandler(file, root, db)
            file_handler.bulk_insert(engine)
            print(f"Table `{file}` updated ")

    crawler(path, to_sql)
