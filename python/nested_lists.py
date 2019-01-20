# Enter your code here. Read input from STDIN. Print output to STDOUT
s1=[]
for _ in range(int(raw_input())):
    s1.append([raw_input(),float(raw_input())])
a=sorted(set([marks for name, marks in s1]))[1]
for i in sorted(s1):
    if a in i:
        print i[0]
