# Enter your code here. Read input from STDIN. Print output to STDOUT
print((lambda x,y:y[-2] )(raw_input(),list(sorted(set(map(int,raw_input().split()))))))
