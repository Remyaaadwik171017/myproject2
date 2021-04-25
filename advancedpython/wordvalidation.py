#combination of uppercase and lowercase letter ending with a no
import re
n=input("Enter a word to validate:")
x="([a-zA-Z]+[0-9]{1}$)"
match=re.fullmatch(x,n)
if match is not None:
    print("valid:",n)
else:
    print("Not valid:",n)