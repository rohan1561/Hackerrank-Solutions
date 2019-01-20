# Enter your code here. Read input from STDIN. Print output to STDOUT
scores={}
for _ in range(int(raw_input())):
    a=raw_input().split()
    scores[a[0]]=sum(map(float, a[1:]))/3
print '%.2f'%(scores[raw_input()])
    
