import mysql.connector
mc=mysql.connector.connect(host="localhost",user="root",password="mrithula",database="online_shopping_management")
mr=mc.cursor()
mr.execute("insert into staff(staffid,name,phone,email_id,password)values(101,'amir','9765385311','mir@gmail.com','mir05')")
mr.execute("insert into staff(staffid,name,phone,email_id,password)values(102,'madhumitha','7642146896','mith@gmail.com','madhu')")
mr.execute("insert into staff(staffid,name,phone,email_id,password)values(103,'raju','8876424672','12raj@gmail.com','rock_it')")
mr.execute("insert into staff(staffid,name,phone,email_id,password)values(104,'niroop','9987487960','nir23@gmail.com','12roop')")
mc.commit()
print(mr.rowcount,'records inserted')
