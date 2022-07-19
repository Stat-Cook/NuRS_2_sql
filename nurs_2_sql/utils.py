import pandas as pd


reader_dict = {
    ".csv": pd.read_csv,
    ".tsv": lambda path: pd.read_csv(path, sep="\t"),
    ".xls": lambda path: pd.read_excel(path, sheet_name=None),
    ".xlsb": lambda path: pd.read_excel(path, sheet_name=None),
    ".xlsx": lambda path: pd.read_excel(path, sheet_name=None)
}

default_dict = dict(
    dialect="mysql",
    username="nurs_2_sql",
    password="password",
    host="localhost",
    port=3306
)
