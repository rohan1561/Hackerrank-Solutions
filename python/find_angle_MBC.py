# Enter your code here. Read input from STDIN. Print output to STDOUT
sample=raw_input()
arr=[]
l=int(raw_input())
for i in range(0,len(sample),l):
    arr.append(sample[i:i+l])
for i in arr:
    x=''
    lis=list(i)
    for j in range(len(set(lis))):
        x+=lis[0]
        lis=filter(lambda m:m!=lis[0],lis)
    print x
