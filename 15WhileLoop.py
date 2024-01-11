#simple while loop demonstration(sum of n natural numbers)
n=int(input("Enter n: "))
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print("The sum is",sum)
