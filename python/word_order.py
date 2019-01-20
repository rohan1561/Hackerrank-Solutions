from collections import Counter
n=int(raw_input())
list=[]
for i in range(n):
    list.append(*raw_input().split())
print len(set(list))
counts=Counter(list)
for i in list:
    x=counts.pop(i,None)
    if x==None:
        continue
    else:
        print x,
