from functools import reduce
lst=[10,20,30,12]
total=reduce(lambda no1,no2:no1+no2,lst)
print(total)

mx=reduce(lambda no1,no2:no1 if no1>no2 else no2,lst)
print(mx)

min=reduce(lambda no1,no2:no1 if no1<no2 else no2,lst)
print(min)