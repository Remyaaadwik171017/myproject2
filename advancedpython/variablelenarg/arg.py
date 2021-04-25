def print_persondetails(**kwargs):
    print(kwargs)

res=print_persondetails(name="arun",place="ktym",wrk="lt")

#** used for n number of variables and read as dictionary. while * reads as tuple

def print_persondetail(*args):
    print(args)

res1=print_persondetail("arun","ktym","lt")