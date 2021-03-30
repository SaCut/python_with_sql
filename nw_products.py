import pyodcb

class Products():
    def __init__(self, server, database, username, password, table_name="saverio_table"):
        self.dock = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER='
            + server
            + ';DATABASE='
            + database
            + ';UID='
            + username
            + ';PWD='
            + password)

        self.name = table_name
        
        self.cursor = self.dock.cursor()

    def _cols_and_data(self, *args, *varbs):
        cols = ""
        values = ""

        for arg in args:
            cols += str(arg) + ","

        for var in varbs:
            values += str(var) + ","

        return (cols, values)

    def create_table(self, name=self.name, cursor=self.cursor):
        cursor.execute(f"CREATE TABLE {name};")

    def insert_data(self, name=self.name, cursor=self.cursor, *args, *varbs):
        cols = self._cols_and_data(*args, *varbs)[0]
        values = self._cols_and_data(*args, *varbs)[1]
        
        cursor.execute(f"INSERT INTO {name} ({cols}) VALUES ({values})")

    def update_data(self, name=self.name, cursor=self.cursor, col, *varbs):
        cols = self._cols_and_data(*args, *varbs)[0]
        values = self._cols_and_data(*args, *varbs)[1]

        cursor execute(f"UPDATE {name} SET {col} = ({values})")

    def delete_data(self, name=self.name, cursor=self.cursor, col, condition):
        cols = self._cols_and_data(col, *varbs)[0]
        values = self._cols_and_data(col, *varbs)[1]

        cursor.execute(f"DELETE FROM {name} WHERE {col}='condition';")


