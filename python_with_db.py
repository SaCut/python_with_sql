# import PYODBC
import pyodbc

# let's establish the connection using pyodbc
server = "18.135.103.95"

database = "Northwind"

username = "SA"

password = "Passw0rd2018"

docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = docker_Northwind.cursor()

print(cursor.execute("SELECT @@version;"))