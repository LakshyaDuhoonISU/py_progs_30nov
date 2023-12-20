#WAP to find the LCM of two user entered number
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
if a>b:
    c=a
else:
    c=b
while True:
    if c%a==0 and c%b==0:
        lcm=c
        break
    c+=1
print("LCM of",a,"and",b,"is",lcm)