#a wor starting with a ending with b
import re
n=input("Enter a word to validate:")
x="(^a[a-zA-Z0-9\W]*[b]$)"
match=re.fullmatch(x,n)
if match is not None:
    print("valid:",n)
else:
    print("Not valid:",n)