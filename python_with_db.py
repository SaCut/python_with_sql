# import PYODBC
import pyodbc

# let's establish the connection using pyodbc
server = "18.135.103.95"

database = "Northwind"

username = "SA"

password = "Passw0rd2018"

docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = docker_Northwind.cursor()

cursor.execute("SELECT @@version;")

# let's fetch some data from Northwind db
row = cursor.fetchone()

# print(row)

# let's connect to out db and fetch some data from Customers table
# cust_rows = cursor.execute("SELECT * FROM Customers").fetchall() # fetchall to take everything from the table

# print(cust_rows)

# prod_rows = cursor.execute("SELECT * FROM Products").fetchall()

# # each row of a column becomes an element of a list in the attribute (named after the column)
# for row in prod_rows:
# 	print(row.UnitPrice)

rows = cursor.execute("SELECT * FROM Products")

while True:
	row = rows.fetchone()
	if row is None:
		break
	print(row.UnitPrice)