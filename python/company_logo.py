# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
x=Counter(list(raw_input().strip()))
x=sorted(x.items(),key=lambda t:t[1],reverse=True)
if x[0][1]==x[2][1]:
    x=sorted(x)
for i in range(3):
    print x[i][0],x[i][1]
