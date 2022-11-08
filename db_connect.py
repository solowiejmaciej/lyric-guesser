import mysql.connector
db = mysql.connector.connect(
    host='146.59.86.9',
    user='Maciej',
    password='Sledz1926!',
    database='lyricguesser',
    charset='utf8mb4'
)

cursor = db.cursor()
#https://pynative.com/python-mysql-database-connection/

#Do poprawnieia 

#ALTER TABLE songs AUTO_INCREMENT = 1