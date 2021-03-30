from nw_products import Products

sql_product = Products("server", "username", "database", "password")

sql_product.create_table(, )
sql_product.insert_data(args="column1", args="column2", args="columnN", values="value1", values="value2", values="valueN")
sql_product.update_data(col="column", values="value1", values="value2", values="valueN")
sql_product.delete_data(col="column", condition="condition")
