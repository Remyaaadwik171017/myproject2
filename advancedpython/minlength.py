#min length 8 max length15
import re
n=input("Enter a word to validate:")
x=len(n)
print(x)
if 8<x>15:
    x="([\w][\d][\W]*$)"
    match=re.fullmatch(x,n)
    if match is not None:
        print("valid:",n)
    else:
        print("Not valid:",n)
else:
    print("not valid",n)