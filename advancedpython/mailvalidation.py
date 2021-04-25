import re
n=input("enter mail to validate:")
r="([a-zA-Z0-9_.+-]+@+[a-zA-Z0-9]+\.[a-zA-Z0-9]+$)"
matcher=re.fullmatch(r,n)
if matcher is not None:
    print("valid mail:",n)
else:
    print("not valid",n)