import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    database="mydb",
    auth_plugin="mysql_native_password",


)

cursor=db.cursor()
f=open("empdetails")
for lines in f:
    data=lines.rstrip("\n").split(",")
    sql="insert into employe(eid,ename,desig,salary)values(%s,%s,%s,%s)"
    cursor.execute(sql,tuple(data))
    db.commit()
db.close()