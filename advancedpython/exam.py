import re
n=input("Enter a word to validate:")
x="[A-Z]+[a-z]+$"
match=re.fullmatch(x,n)
if match is not None:
    print("valid:",n)
else:
    print("Not valid:",n)
