# Enter your code here. Read input from STDIN. Print output to STDOUT
a=map(int,raw_input().split())
t=a[-1]
a=a[:-1]
for i in range(t-len(a)):
    a.append(a[-2:][0]+(a[-2:][1])**2)
print a[-1]
