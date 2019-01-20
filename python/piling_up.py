for _ in xrange(int(raw_input())):
    marker = 0
    x = int(raw_input())
    y = map(int, raw_input().split())
    i = 0
    if len(y) == 2:
        print 'Yes'
        continue
    elif len(y) == 3 and y[1] > y[0]:
        if y[1]>y[2]:
            marker = 1
    while i < len(y)/2 - 1:
        if y[i] >= y[i+1]:
            i += 1
            continue
        else:
            marker = 1
            break
        i += 1
    while i <= len(y)-1 and i >= len(y)/2:        
        if y[i] <= y[i+1]:
            i += 1
            continue
        else:
            marker = 1
            break
        
    if marker == 0:
        print 'Yes'
    else:
        print 'No'
