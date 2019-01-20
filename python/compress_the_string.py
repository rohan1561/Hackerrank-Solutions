# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
for i,j in itertools.groupby(raw_input()):
    print (len(list(j)),int(i)),
