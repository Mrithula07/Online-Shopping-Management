import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="mrithula",database="online_shopping_management")
cur=con.cursor()
cur.execute("CREATE TABLE staff(staffid int(3) Primary key,name varchar(25),phone varchar(11),email_id varchar(25),password varchar(10))")



