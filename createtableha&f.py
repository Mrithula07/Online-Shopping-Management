import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="mrithula",database="online_shopping_management")
mycursor=con.cursor()
mycursor.execute("CREATE TABLE homeappliance_and_furniture (hfid varchar(5) Primary key, name varchar(25), status varchar(25), specification varchar(70),price int(10))")
