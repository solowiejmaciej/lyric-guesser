import mysql.connector
db = mysql.connector.connect(
    host='',
    user='',
    password='',
    database='',
    charset='utf8mb4'
)

cursor = db.cursor()
#https://pynative.com/python-mysql-database-connection/

#Do poprawnieia 

#ALTER TABLE songs AUTO_INCREMENT = 1
