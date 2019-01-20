# Enter your code here. Read input from STDIN. Print output to STDOUT
print((lambda a,b,c,d: sum([(i in c)-(i in d) for i in b]))(map(int, raw_input().strip().split()), map(int, raw_input().strip().split()), set(map(int, raw_input().strip().split())), set(map(int, raw_input().strip().split()))))
