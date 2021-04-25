import re
x="a{1,3}"
r="aaa aab aaan"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())
