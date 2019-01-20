from itertools import combinations
a,b,c=int(raw_input()), raw_input().split(),int(raw_input())
print float(len(filter(lambda x: 'a' in x,combinations(b,c))))/len(list(combinations(b,c)))
