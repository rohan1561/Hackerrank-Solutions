import re
def validate(x):
    return (bool(re.search(r'^[456]',x)) and bool(re.search(r'^\d{16}$',x) or re.search(r'^\d{4}\-\d{4}\-\d{4}\-\d{4}$',x)) and bool(re.search(r'(\d)\-{0,1}\1\-{0,1}\1\-{0,1}\1',x))==False)
for i in range(int(raw_input())):
    print 'Valid' if validate(raw_input())==True else 'Invalid'
