# Python with SQL

#### Establishing a connection with PYODBC
- ![img](https://raw.githubusercontent.com/SaCut/python_with_sql/main/Python_with_SQL.png)
- This link is useful if there are any errors:
https://packages.microsoft.com/ubuntu/20.04/prod/pool/main/m/msodbcsql17/

```python
# import PYODBC
import pyodbc

# let's establish the connection using pyodbc
server = "**.***.***.**"

database = "Northwind"

username = "SA"

password = "************"

docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = docker_Northwind.cursor()

cursor.execute("SELECT @@version;")

# let's fetch some data from Northwind db
row = cursor.fetchone()

print(row)

# let's connect to out db and fetch some data from Customers table
cust_rows = cursor.execute("SELECT * FROM Customers").fetchall() # fetchall to take everything from the table

print(cust_rows)

prod_rows = cursor.execute("SELECT * FROM Products").fetchall()

# each row of a column becomes an element of a list in the attribute (named after the column)
for row in prod_rows:
    print(row.UnitPrice)

rows = cursor.execute("SELECT * FROM Products")

while True:
    row = rows.fetchone()
    if row is None:
        break
    print(row.UnitPrice)


# close the database when you leave
docker_Northwind.close()
```

### SQL OOP task

#### Timings

25 - 30

* OOP example using pyodbc

create an example of how we can create service objects related to a particular table.

#### An sql manager for the products table

create an object that relates only to the products table in the Northwind database. The reason for creating a single object for any table within the database would be to ensure that all functionality we build into this relates to what could be defined as a 'business function'.

As an example the products table, although relating to the rest of the company, will service a particular area of the business in this scenario we will simply call them the 'stock' department. 

The stock department may have numerous requirements and it makes sense to contain all the requirements a code actions within a single object.

Create two files `nw_products.py` & `nw_runner.py` and then we will move into creating our object.

APPLY OOP - DRY CRUD WHERE POSSIBLE

#### Solution
