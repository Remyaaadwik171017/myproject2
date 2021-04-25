def div_deco(fun):
    def wrapper(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)
        return fun(n1,n2)
    return wrapper

@div_deco
def division(num1,num2):
    return (num1/num2)
r=division(2,10)
print(r)
