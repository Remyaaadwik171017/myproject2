def decorator_sub(fun):
    def inner(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)
        return fun(n1,n2)
    return inner

@decorator_sub
def sub(num1,num2):
    return num1-num2
res=sub(20,100)
print(res)