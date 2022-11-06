import sqlite3


class Database:

    def __init__(self, database_name: str):
        self.con = sqlite3.connect(database_name)
        self.cursor = self.con.cursor()
        self.indexes_in_table = []

        self.cursor.execute('''SELECT name FROM sqlite_master WHERE type='table';''')
        self.tables_names = self.cursor.fetchall()

    def __del__(self):
        self.con.close()

    def update_set_of_tables(self):
        self.cursor.execute('''SELECT name FROM sqlite_master WHERE type='table';''')
        self.tables_names = self.cursor.fetchall()

    def check_if_t_name_valid(self) -> bool:
        '''
        Check if table name is not empty and available in data base.
        '''
        if self.table_name == '':
            print("\nTable name can not be empty!\n")
            return False

        if (self.table_name,) in self.tables_names:
            print("\nGiven table name is already defined in data base!\n")
            return False

        return True

    def create_table(self):
        self.table_name = input("\nEnter new table name: ")
        if self.table_name:
            if self.check_if_t_name_valid():
                columns = ["id INTEGER PRIMARY KEY AUTOINCREMENT"]

                columns.append(input("\nEnter names of colums and their types in table separated by coma sign.\n"
                                "First column is automaticly added as: id INTEGER PRIMARY KEY AUTOINCREMENT\n"
                                "\nColumns: "))

                self.cursor.execute(f'''CREATE TABLE {self.table_name} ({", ".join(columns)})''')
                self.con.commit()
                print(f"\nTable with name '{self.table_name}' created in data base!\n")

        self.update_set_of_tables()

    def flsk_create_table(self, t_name: str, clmns: str):
        self.table_name = t_name
        if self.check_if_t_name_valid():
            columns = ["id INTEGER PRIMARY KEY AUTOINCREMENT"]

            columns.append(clmns)

            self.cursor.execute(f'''CREATE TABLE {self.table_name} ({", ".join(columns)})''')
            self.con.commit()
            print(f"\nTable with name '{self.table_name}' created in data base!\n")

        self.update_set_of_tables()

    def fetch_tables_names(self) -> list:
        self.cursor.execute('''SELECT name FROM sqlite_master WHERE type='table';''')
        tables = self.cursor.fetchall()
        #print("\nTables in database:", *tables, "\n")
        return tables

    def delete_table(self):
        self.table_name = input("Enter name of table to detele from data base: ")
        if self.table_name == "":
            print("\nTable name can not be empty!\n")

        if (self.table_name,) in self.tables_names:
            self.cursor.execute(f'''DROP TABLE {self.table_name}''')
            print("\nTable deleted from data base\n")
        else:
            print("\nEntered name of table is not available in data base!\n")

        self.update_set_of_tables()

    def fetch_columns(self, table_name: str) -> list:
        self.cursor.execute(f'''PRAGMA table_info({table_name})''')
        columns = self.cursor.fetchall()
        columns = [col_name[1] + " " + col_name[2] for col_name in columns]
        print("COLUMNS: ", columns)
        return columns

    def fetch_records(self, table_name: str) -> list:
        records = [record for record in self.cursor.execute(f'''SELECT * FROM {table_name}''')]
        return records

    def fetch_all_indexes_in_table(self, table_name: str) -> list:
        records = [record for record in self.cursor.execute(f'''SELECT * FROM {table_name}''')]
        self.indexes_in_table = [str(index[0]) for index in records]
        return self.indexes_in_table


    def add_record(self, table_name: str, num_of_columns: int, column_names: list) -> bool:
        prepare_pattern = num_of_columns*["?"]
        column_types = [kolumn.split() for kolumn in column_names[1:]]
        column_types_to_print = [type[0] + " " + type[1] for type in column_types]
        column_types_to_check = [type[1] for type in column_types]

        user_data = input(f"\nEnter data separated by coma in correct type in following order: {column_types_to_print}: ")
        user_data = user_data.split(",")

        if len(user_data) != len(column_types):
            print("\nNumber of enterad data is not equal to number of columns in table!\n")
            print(f"Number of entered data: {len(user_data)}")
            print(f"Number of columns in table: {len(column_types)}\n")
            return None

        cnt = 0
        for data_type in column_types_to_check:
            if data_type == "Int" or data_type == "int":
                try:
                    user_data[cnt] = int(user_data[cnt])
                except:
                    print("\nEntered data has no correct type!")
                    return None

            elif  data_type == "Real" or data_type == "real":
                try:
                    user_data[cnt] = float(user_data[cnt])
                except:
                    print("\nEntered data has no correct type!")
                    return None

            cnt += 1

        user_data.insert(0, None)

        self.cursor.execute(f'''INSERT INTO {table_name} VALUES ({",".join(prepare_pattern)})''', tuple(user_data))
        self.con.commit()

        return True

    def flsk_add_record(self, table_name: str, num_of_columns: int, column_names: list, record_data: str):
        prepare_pattern = num_of_columns * ["?"]
        column_types = [kolumn.split() for kolumn in column_names[1:]]
        column_types_to_check = [type[1] for type in column_types]

        user_data = record_data
        user_data = user_data.split(",")

        if len(user_data) != len(column_types):
            print("\nNumber of enterad data is not equal to number of columns in table!\n")
            print(f"Number of entered data: {len(user_data)}")
            print(f"Number of columns in table: {len(column_types)}\n")
            return None

        cnt = 0
        for data_type in column_types_to_check:
            if data_type == "Int" or data_type == "int":
                try:
                    user_data[cnt] = int(user_data[cnt])
                except:
                    print("\nEntered data has no correct type!")
                    return None

            elif data_type == "Real" or data_type == "real":
                try:
                    user_data[cnt] = float(user_data[cnt])
                except:
                    print("\nEntered data has no correct type!")
                    return None

            cnt += 1

        user_data.insert(0, None)

        self.cursor.execute(f'''INSERT INTO {table_name} VALUES ({",".join(prepare_pattern)})''', tuple(user_data))
        self.con.commit()

    def del_record_by_index(self, table_name):
        index = input("\nEnter index of record to delete: ")
        if index == "":
            return "\nNo parameter was given!"

        if not index.isnumeric():
            return "\nWrong parameter. Given parameter is not numeric type!"

        self.fetch_all_indexes_in_table(table_name)
        if len(self.indexes_in_table) == 0:
            return "\nTable is empty. There is no any record!"
        else:
            if not index in self.indexes_in_table:
                return "\nThere is no record with given index number in table!"
            else:
                sql_command = f'''DELETE FROM {table_name} WHERE id=?'''
                self.cursor.execute(sql_command, index)
                # Why UPDATE of primary key not work?
                sql_command = f'''UPDATE sqlite_sequence SET seq = 1 WHERE name = "{table_name}"'''
                self.cursor.execute(sql_command)

                self.con.commit()
                return "\nRecord deleted correctly"

    def flsk_del_record_by_index(self, table_name: str, index: str) -> str:
        if index == "":
            return "No parameter was given!"

        if not index.isnumeric():
            return "Wrong parameter. Given parameter is not numeric type!"

        self.fetch_all_indexes_in_table(table_name)
        if len(self.indexes_in_table) == 0:
            return "Table is empty. There is no any record!"
        else:
            if not index in self.indexes_in_table:
                return "There is no record with given index number in table!"
            else:
                sql_command = f'''DELETE FROM {table_name} WHERE id=?'''
                self.cursor.execute(sql_command, index)
                self.con.commit()
                return "Record deleted correctly"

    def delete_all_records_in_table(self, table_name: str):
        sql_command = f'''DELETE FROM {table_name}'''
        self.cursor.execute(sql_command)
        row_counter = self.cursor.rowcount

        sql_command = f'''DELETE FROM sqlite_sequence WHERE name = "{table_name}"'''
        self.cursor.execute(sql_command)
        self.con.commit()

        return f"\nDeleted {row_counter} records from table"