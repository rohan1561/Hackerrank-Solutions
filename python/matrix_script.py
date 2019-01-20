# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
a,b=map(int,raw_input().split())
x=[]
for _ in range(b):
    x.append('')
for i in range(a):
    y=raw_input()
    for j in range(b):
        x[j]+=y[j]
x=''.join(i for i in x)
z=re.sub(r'(?<=[a-zA-Z])[\s\!@#\$%&]+(?=[a-zA-Z])',' ',x)
print z
