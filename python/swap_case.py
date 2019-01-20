# Enter your code here. Read input from STDIN. Print output to STDOUT
print ''.join([i.lower() if i.isupper() else i.upper() for i in raw_input()])
