#WAP to print pyramid pattern
#num=int(input("Enter number of rows: "))
'''for i in range(1,num+1): #ascending half pyramid
    for j in range(i):
        print(" * ",end='')
    print("\n")

for i in range(num-1,0,-1): #descending half pyramid
    for j in range(i):
        print(" * ",end='')
    print("\n")'''

'''for i in range(1,num+1):
    for j in range(num,i,-1): #pyramid pattern ascending
        print(" ",end='')
    for k in range(2*i-1):
        print("*",end='')
    print()'''

'''for i in range(0,num): #pyramid pattern descending
    for j in range(i):
        print(" ",end='')
    for k in range(2*(num-i)-1):
        print("*",end='')
    print()'''

'''ascii_no=65 #alphabetical half pyramid ascending pattern
for i in range(0,num):
    for j in range(0,i+1):
        print(chr(ascii_no),end='')
        ascii_no+=1
    print()'''

'''ascii_no=65 #alphabetical half pyramid ascending pattern
for i in range(0,num):
    for j in range(0,i+1):
        print(chr(ascii_no),end='')
    print()
    ascii_no+=1'''

'''for i in range(1,num+1): #hollow diamond pattern 
    for j in range(num,i,-1): 
        print(" ",end='')
    for k in range(2*i-1):
        if k==0 or k==2*i-2:
            print("*",end='')
        else: 
            print(" ",end='')
    print()
for i in range(1,num): 
    for j in range(i):
        print(" ",end='')
    for k in range(2*(num-i)-1):
        if k==0 or k==2*(num-i)-2:
            print("*",end='')
        else:
            print(" ",end='')
    print()'''

'''for i in range(1,5+1): #star pattern
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
    print()'''

'''    for l in range(5):
        if l==5-i:
            print(" * ",end='')
        else:
            print("    ",end='')'''
'''for i in range(1,num+1):
    for j in range(i+1):
        print(" * ",end='')
    print()'''

"""
star j==1+4*i or
"""
# x=int(input("enter the rows "))

'''for i in range(1,5+1):
    for n in range(14):
        print(" ",end="")
    for j in range(5,i,-1):
        print(" ",end="")
    for k in range(2*i-1):
        if k==0 or k==2*i-2 :
            print("$",end="")
        else:
            print(" ",end="") 
    print(" ")
    for n in range(14):
        print(" ",end="")
    for j in range(5,i,-1):
        print(" ",end="")
    for k in range(2*i):
        if k==2*i-1 :
            print(" ",end="")
        else:
            print(" ",end="") 
    print(" ")

for i in range(1):
    for j in range(14):
       print("$",end="  ")
    print("")
for i in range(6):
    for j in range(1,39):
        if j==13-i or j==24+i :
            # or j==6*i+1 or j==40-6*i-2
            print("$",end=" ")
            # print(" ",end="")
        else:
            print(" ",end="")
    print(" ")    
    for j in range(1,39):
        if j==6*i+1 or j==40-6*i-3:
            print("$",end="")
            # print(" ",end="")
        else:
            print(" ",end="")
    print(" ")'''

