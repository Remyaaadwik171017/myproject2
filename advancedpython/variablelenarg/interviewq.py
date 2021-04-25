employee={
    1000: {"name":"sabir","des":"develpoer","exp":3},
    1001: {"name":"remya","des":"designer","exp":4},
    1002: {"name":"sarath","des":"develper","exp":2},
    1003: {"name":"sabitha","des":"bigdata","exp":3},

}
def print_empdetails(**kwargs):
    id=kwargs["eid"]
    prop=kwargs["prop"]
    if id in employee:
        print(employee[id]["name"])
        print(employee[id][prop])
    else:
        print("not exist")
res=print_empdetails(eid=1000,prop="des")