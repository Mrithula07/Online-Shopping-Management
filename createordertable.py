import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="mrithula",database="online_shopping_management")
cur=con.cursor()
cur.execute("CREATE TABLE orders_table(cid int(3),oid int(5),name varchar(25),price int(10))")
