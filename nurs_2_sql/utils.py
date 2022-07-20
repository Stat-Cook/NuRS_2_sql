import pandas as pd


reader_dict = {
    ".csv": pd.read_csv,
    ".tsv": lambda path: pd.read_csv(path, sep="\t"),
    ".xls": lambda path: pd.read_excel(path, sheet_name=None),
    ".xlsb": lambda path: pd.read_excel(path, sheet_name=None),
    ".xlsx": lambda path: pd.read_excel(path, sheet_name=None)
}

default_dict = dict(
    drivername = "mssql+pyodbc",
    username = "",
    password = "",
    host = "localhost//SQLEXPRESS",
    port = "",
    database = "DEFAULT",
    driver = "ODBC Driver 17 for SQL Server"
)
