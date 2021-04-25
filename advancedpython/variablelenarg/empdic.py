employee={
    1000: {"name":"sabir","des":"develpoer","exp":3},
    1001: {"name":"remya","des":"designer","exp":4},
    1002: {"name":"sarath","des":"develper","exp":2},
    1003: {"name":"sabitha","des":"bigdata","exp":3},

}

eid=int(input("enter your eid: "))
if (eid in employee):
    print (employee[eid]["name"])
else:
    print("eid not exist")