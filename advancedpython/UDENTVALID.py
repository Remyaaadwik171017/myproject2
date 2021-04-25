import re
f=open("student","r")
for lines in f:
    data=lines.rstrip("\n")
    x="[lL][uU][Mm]\d{2}[pP][Yy]\d{3}"
    match=re.fullmatch(x,data)
    if match is not None:
        print("valid:",data)
        f1 = open("pythonstudents","a")
        f1.write(data)
        f1.write("\n")
    else:
        print("not valid:",data)
