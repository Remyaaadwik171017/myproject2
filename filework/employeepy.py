class Employee:
    def __init__(self,eid,ename,desig,salary):
        self.eid=eid
        self.ename=ename
        self.desig=desig
        self.salary=salary
    def printvalue(self):
        print(self.ename)
f=open("employee")
e1=Employee(1000,"arun","developer",25000)
e2=Employee(1001,"arjun","developer",26000)
e3=Employee(1002,"varun","qa",27000)
e4=Employee(1001,"vivek","mrkt",28000)
employees=[]
employees.append(e1)
employees.append(e2)
employees.append(e3)
employees.append(e4)
salary=[]
for emp in employees:
    salary.append(emp.salary)
highsal=max(salary)
print(highsal)
if(emp.salary==highsal):
        print(emp.ename,"=>",emp.eid,"=>",emp.desig,"=>",emp.salary)
