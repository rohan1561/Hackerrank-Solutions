# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
a=[]
for i in range(int(raw_input())):
    a.append(raw_input())
for i in a:
    i=re.sub(r'(?<=\s)(&&)(?=\s)','and',i)
    i=re.sub(r'(?<=\s)(\|\|)(?=\s)','or',i)
    print i
