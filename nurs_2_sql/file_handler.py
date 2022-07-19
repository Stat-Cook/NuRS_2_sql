import pandas as pd
import os

from .utils import reader_dict


class FileHandler:

    def __init__(self, file, path, db="Dev"):
        self.path = path
        self.file = file
        _, self.ext = os.path.splitext(file)
        self.db = db

    @property
    def reader(self):
        return reader_dict[self.ext]

    @property
    def data(self) -> pd.DataFrame:
        rel_path = os.path.join(self.path, self.file)
        return self.reader(rel_path)

    @property
    def relative_file_path(self):
        return os.path.join(
            self.path,
            self.file
        )

    @property
    def table(self):
        return ".".join([self.db, self.file])

    def to_sql(self, engine, head=5):
        self.data.head(head).to_sql(
            self.table, con=engine, schema=self.db, if_exists='replace', index=False)
        return 0

    def delete_sql_rows(self, engine):
        with engine.connect() as con:
            delete_statement = f"Delete from {self.table};"
            con.execute(delete_statement)

        return 0

    def bulk_insert(self, engine):
        bulk_insert_statement =  \
            f"" \
            f"bulk insert {self.table} " \
            f"from '{self.relative_file_path}' " \
            f"WITH " \
            f"(FIRSTROW = 2);"

        with engine.connect() as con:
            con.execute(bulk_insert_statement)
        return 0

