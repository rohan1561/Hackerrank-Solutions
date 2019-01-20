# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
def valid(x):
    return(bool(re.search(r'^[1-9]\d{5}$',x)) and len(re.findall(r'(?=(\d).{1}\1)',x))<=1)
print valid(raw_input())
