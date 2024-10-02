import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="mrithula",database="online_shopping_management")
cur=con.cursor()
cur.execute("CREATE TABLE electronics(eid int(5) Primary key,name varchar(25),status varchar(20),brand varchar(50),price int(10))")
