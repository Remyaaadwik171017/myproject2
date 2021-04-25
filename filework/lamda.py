lst=[10,20,30,21,22]
squ=[]
for num in lst:
    res=num**2
    squ.append(res)
print(squ)

#map()
#filter()
#reduce()

lst=[10,20,30,21,22]
squares=list(map(lambda no:no**2,lst))
print(squares)

cube=list(map(lambda no:no**3,lst))
print (cube)