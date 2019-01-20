# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
[a,b]=map(int,raw_input().split())
z=[]
y=[]
for _ in range(a):
    z.append(map(lambda t: t**2,map(int,raw_input().split())[1:]))  #list of lists of squares of every input
for i in list(product(*z)):                                         #refer itertools.product
    y.append(sum(i)%b)                                              
print max(y)

    
