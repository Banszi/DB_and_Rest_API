

class Db_manager:

    def __init__(self, db_name: str):
        self.db_name = db_name
        print(f"Your Database name: {self.db_name} \n")

    def run_manager_general(self) -> str:
        print("Select one of given operations: \n")
        print("1. Fetch all tables names")
        print("2. Create new table")
        print("3. Select table by name")
        print("4. Delete table by name")
        print("5. End program \n")

        operation = input("Your choice: ")
        return operation

    def run_menager_special(self) -> str:
        print("\nSelect one of given operations: \n")
        print("1. Fetch all column names in table")
        print("2. Fetch all records in table")
        print("3. Add record to table")
        print("4. Delete record from table by index")
        print("5. Delete all records from table")
        print("6. Back to previous operation list")
        print("7. End program \n")

        operation = input("Your choice: ")
        return operation