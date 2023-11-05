import mysql.connector

# conn = mysql.connector.connect(host="127.0.0.1", user="root", password="")
# cousor = conn.cursor()
# cursor.execute(
#     "create database test_mysql_database"
# )
# cursor.close()
# conn.close()

conn = mysql.connector.connect(host="127.0.0.1", database="test_mysql_database")
cursor = conn.cursor()

cursor.execute('insert into persons(name) values("Mike")')
conn.commmit()

cursor.execute("select * from persons")
for row in cursor:
    print(row)
