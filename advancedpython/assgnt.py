import re
f=open("asgnt","r")
for lines in f:
    data=lines.rstrip("\n")
    x="[a-zA-Z]{2}\d{2}[a-zA-Z]{2}\d{4}"
    match=re.fullmatch(x,data)
    if match is not None:
        print("valid:",data)
    else:
        print("not valid:",data)


