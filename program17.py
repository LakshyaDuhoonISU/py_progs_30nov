#WAP to check prime numbers in a given range(using for loop)
a=int(input("Enter starting range: "))
b=int(input("Enter ending range: "))
if a<b:
    for i in range(a,b+1):
        count=0
        for j in range(2,i):
            if i%j==0:
                count+=1
        if count==0:
            print(i)
else:
    for i in range(a,b-1,-1):
        count=0
        for j in range(2,i):
            if i%j==0:
                count+=1
        if count==0:
            print(i)