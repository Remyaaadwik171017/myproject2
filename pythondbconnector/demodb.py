#mysql connector

#import mysql module
import mysql.connector
#establish connection
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    auth_plugin="mysql_native_password"
)
#create curser object
cursor=db.cursor()
#sql quieries excecute
sql="select version()"
cursor.execute(sql)
data=cursor.fetchone()
print(data)
db.close()
#close established connection