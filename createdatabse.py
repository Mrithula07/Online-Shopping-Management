import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="mrithula")
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE online_shopping_management")
