from os import getenv
from dotenv import load_dotenv
from database import Database

load_dotenv()

db_name = getenv("DB_NAME")


def fetch_table_names() -> list:
    DB = Database(db_name)
    db_table_names = DB.fetch_tables_names()
    db_table_names = [tab[0] for tab in db_table_names]
    return db_table_names

def create_new_table():
    DB = Database(db_name)
    DB.create_table()

def tables_names_in_db():
    DB = Database(db_name)
    return DB.tables_names

def fetch_all_columns(table_name: str):
    DB = Database(db_name)
    return DB.fetch_columns(table_name)

def fetch_all_records(table_name: str):
    DB = Database(db_name)
    return DB.fetch_records(table_name)

def add_new_record(table_name, num_of_columns, columns_names):
    DB = Database(db_name)
    DB.add_record(table_name, num_of_columns, columns_names)

def del_record(table_name: str):
    DB = Database(db_name)
    return DB.del_record_by_index(table_name)

def del_table():
    DB = Database(db_name)
    DB.delete_table()

def create_new_table_flsk(table_name: str, columns: str):
    DB = Database(db_name)
    DB.flsk_create_table(table_name, columns)

def add_new_record_flsk(table_name: str, record_data: str):
    DB = Database(db_name)
    columns_names = fetch_all_columns(table_name)
    num_of_columns = len(columns_names)
    DB.flsk_add_record(table_name, num_of_columns, columns_names, record_data)

def fetch_columns_in_table_flsk(table_name: str):
    DB = Database(db_name)
    return DB.fetch_columns(table_name)

def fetch_records_in_table_flsk(table_name: str):
    DB = Database(db_name)
    return DB.fetch_records(table_name)

def delete_record_by_index_flsk(table_name: str, index: str):
    DB = Database(db_name)
    return DB.flsk_del_record_by_index(table_name, index)

def delete_all_records_in_table(table_name: str):
    DB = Database(db_name)
    return DB.delete_all_records_in_table(table_name)
