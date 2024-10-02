import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="mrithula",database="online_shopping_management")
cur=con.cursor()
cur.execute("CREATE TABLE login(cid int(3) Primary key,name varchar(25),email varchar(30),password varchar(10),phone char(10),address varchar(70))")
