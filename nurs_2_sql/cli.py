import argparse

from nurs_2_sql import sql_crawler, bulk_insert_crawler

def cli_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument("path", help='Root path to start crawler from',
                        default=".", nargs="?")

    parser.add_argument("-c", "--conf", help='Path to config file',
                        default="nurs_2_sql.ini", nargs="?")

    parser.add_argument("-i", "--config_id", help='ID in config file to use',
                        default="DEFAULT", nargs="?")

    parser.add_argument("-d", "--db", help='Target database for tables',
                        default="", nargs="?")

    args = parser.parse_args()

    return args


def nurs_2_sql():
    args = cli_parser()
    sql_crawler(args.path, args.conf, args.config_id, args.db)
    return 0


def bulk_insert_cli():
    args = cli_parser()
    bulk_insert_crawler(args.path, args.conf, args.config_id, args.db)

    return 0
