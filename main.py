from os import getenv
from dotenv import load_dotenv
from database import Database
from sys import argv
from db_manager import Db_manager
from flask_urls import *


load_dotenv()


def check_if_oper_correct(operation: str) -> bool:
    if operation.isnumeric():
        return True
    else:
        return False


if __name__ == "__main__":

    manager = Db_manager(db_name)
    print("Hello in your Database manager! \n")

    while True:
        operation = manager.run_manager_general()

        if check_if_oper_correct(operation):
            operation = int(operation)
            if operation == 1:
                db_table_names = fetch_table_names()
                print("\nTables in database:", ", ".join(db_table_names), "\n")


            elif operation == 2:
                create_new_table()

            elif operation == 3:
                table_name = input("\nEnter the name of the table you want to work with: ")
                names = tables_names_in_db()
                if not (table_name,) in names:
                    print("\nGiven name is not available in data base!\n")
                    continue

                while True:
                    operation_inner = manager.run_menager_special()
                    if check_if_oper_correct(operation_inner):
                        operation_inner = int(operation_inner)

                        if operation_inner == 1:
                            columns_names = fetch_all_columns(table_name)
                            print("Columns and their types in table:", ", ".join(columns_names), "\n")

                        elif operation_inner == 2:
                            records = fetch_all_records(table_name)
                            if records:
                                print(f"\nAll records in table: \n")
                                for record in records:
                                    print(str(record[0]) + ":", str(record[1:]))
                            else:
                                print("\nTable is empty. There is no any record!")


                        elif operation_inner == 3:
                            columns_names = fetch_all_columns(table_name)
                            num_of_columns = len(columns_names)
                            oper_result = add_new_record(table_name, num_of_columns, columns_names)
                            if oper_result:
                                print("\nRecord added succesfully!\n")

                        elif operation_inner == 4:
                            command_fb = del_record(table_name)
                            print(command_fb)

                        elif operation_inner == 5:
                            command_fb = delete_all_records_in_table(table_name)
                            print(command_fb)

                        elif operation_inner == 6:
                            '''
                            Back to prev DB maganer list
                            '''
                            break

                        elif operation_inner == 7:
                            '''
                            Close DB maganer
                            '''
                            print("\nDatabase manager closed")
                            exit(0)

            elif operation == 4:
                del_table()

            elif operation == 5:
                print("\nDatabase manager closed")
                break

        else:
            print("\nYour entered wrong number, choose again\n")
