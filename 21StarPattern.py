for i in range(1,5+1): #star pattern
    for l in range(14):
        print(" ",end='')
    for j in range(5,i,-1): 
        print(" ",end='')
    for k in range(2*i-1):
        if k==0 or k==2*i-2:
            print("*",end='')
        else: 
            print(" ",end='')
    print()
for i in range(1):
    for j in range(12):
        print(" * ",end='')
    print()
for i in range(1,5+1):
    for j in range(1,39):
        if j==13-i or j==24+i:
            print("*",end='')
        else:
            print(" ",end='')
    print()
    for k in range(1,39):
        if k==6*i+1 or k==40-6*i-3:
            print("*",end='')
        else:
            print(" ",end='')
    print()
