class Employee:
    def __init__(self,eid,ename,desig,salary):
        self.eid=eid
        self.ename=ename
        self.desig=desig
        self.salary=salary
    def printvalue(self):
        print(self.ename)
e1=Employee(1000,"arun","developer",25000)
e2=Employee(1001,"arjun","developer",26000)
e3=Employee(1002,"varun","qa",27000)
e4=Employee(1001,"vivek","mrkt",28000)
employees=[]
employees.append(e1)
employees.append(e2)
employees.append(e3)
employees.append(e4)
salary=list(map(lambda emp:emp.salary,employees))
print(salary)
maxsalary=max(list(map(lambda emp:emp.salary,employees)))
print(maxsalary)
