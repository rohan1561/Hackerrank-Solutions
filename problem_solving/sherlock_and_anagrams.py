# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def anagram(x,y):                                   #define anagram
    if sorted(x)==sorted(y):
        return True
    else:
        return False
def repeat_acc(a):                                  #accounting for repititions of a single letter separately
    return (math.factorial(a))/(math.factorial(a-2)*2)
for _ in range(int(raw_input())):    
    a=raw_input()
    ans=[]
    for k in range(2,len(a)):                       
        arr=[]
        for i in range(len(a)-k+1):                 #forming segments of the string starting from len=2
            arr.append(a[i:i+k])
        for j in range(len(arr)-1):
            for l in arr[j+1:]:
                ans.append(anagram(arr[j],l))       #checking if the segment arr[j] is an anagram of all subseqent                                                      segments
    for i in set(a):                                #accounting for repititions of a single letter separately
        if a.count(i)>1:
            ans.append(repeat_acc(a.count(i)))
    print sum(ans)
