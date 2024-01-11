#Double pyramid pattern
for i in range(1,6):
    for j in range(6,i,-1): 
        print(" ",end='')
    for k in range(i):
        print("* ",end='')
    for l in range(6,i,-1):
        print(" ",end='')
    for m in range(6,i,-1):
        print(" ",end='')
    for n in range(i):
        print("* ",end='')
    print()
