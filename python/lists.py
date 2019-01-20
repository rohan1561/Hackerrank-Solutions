# Enter your code here. Read input from STDIN. Print output to STDOUT
l=[]
for i in range(int(raw_input())):
    a=raw_input().split()+['','']
    try:
        eval('l.{0}({1},{2})'.format(*a))
    except:
        try:
            eval('l.{0}()'.format(*a))
        except:
            print l
    
    
    
