#mysql connector

#import mysql module
#establish connection
#create curser object
#sql quieries excecute
#close established connection

import mysql.connector
# db=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="Password@123",
#     database="luminar"
# )
# curser=db.cursor()
# sql="create table employee(eid int,ename varchar(50),desig varchar(30),salary int)"
# #sql="insert into employee(eid,ename,desig,salary)values(100,'ajay','developer',10000)"
# # try:
#     curser.execute(sql)
#     db.commit()
# except Exception as e:
#     print(e.args)
#     db.rollback()
# finally:
#     db.close
# db.close
