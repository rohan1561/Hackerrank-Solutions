# Enter your code here. Read input from STDIN. Print output to STDOUT
vowels=['A','E','I','O','U']
a=raw_input()
count=0
count1=0
for i in range(len(a)):
    if a[i] in vowels:
        count+=len(a)-i
    else:
        count1+=len(a)-i
if count1>count:
    print 'Stuart',count1
elif count>count1:
    print 'Kevin', count
else:
    print 'Draw'

