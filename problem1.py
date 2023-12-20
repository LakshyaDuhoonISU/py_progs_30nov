#Aim- To demonstrate 8 types of operators with examples
d=int(input("Select which operator to demonstrate: 1.Arithmetic\n2.Relational\n3.Logical\n4.Identity\n5.Membership\n6.Ternary\n7.Assignment\n8.Bitwise\n"))
if d==1:
    #1. Arithmetic operators
    a=float(input("Enter a number: "))
    b=float(input("Enter another number: "))
    c=input("Which operation you want to perform: +,-,*,/,%,//,**: ")
    if c=="+":
        print("Sum: ",a,"+",b,"=",a+b) # addition operator
    elif c=="-":
        print("Difference: ",a,"-",b,"=",a-b) # subtraction operator
    elif c=="*":
        print("Multiplication: ",a,"*",b,"=",a*b) # multiplication operator
    elif c=="/":
        print("Quotient: ",a,"/",b,"=",a/b) # division operator
    elif c=="%":
        print("Remainder: ",a,"%",b,"=",a%b) # modulus operator
    elif c=="//":
        print("Quotient(without decimal): ",a,"//",b,"=",a//b) # floor operator
    elif c=="**":
        print(a,"^",b,"=",a**b) # power operator
    else:
        print("Wrong option")

elif d==2:
    #2. Relational operators
    a=float(input("Enter first number: "))
    b=float(input("Enter second number: "))
    c=float(input("Enter third number: "))
    if a>b: #Greater than operator
        if a>c:
            print(a,"is the largest number")
        else:
            print(c,"is the largest number")
    elif a<b:  #Less than operator
        if b>c:
            print(b,"is the largest number")
        else:
            print(c,"is the largest number") 
    a=float(input("Enter first number: "))
    b=float(input("Enter second number: "))
    if a==b: print("Both of them are equal") #assignment operator
    else: print("Both of them are not equal")

elif d==3:
    #3. Logical operators
    a=float(input("Enter first number: "))
    b=float(input("Enter second number: "))
    if a>=1 and b>=1: #AND operator
        print("Both of them are positive numbers")
    elif a>=1 or b>=1: #OR operator
        print("One of them is positive")
    else:
        print("Both of them are negative")
        print (not(a>=1 and b>=1))

elif d==4:
    #4. Identity operators
    a=123
    b=a
    c=123
    print(a is b)
    print(a==c)
    print(a is c)

elif d==5:
    #5. Membership operators
    a=input("Enter a string: ")
    b=input("Enter a word to search for: ")
    print(b in a)

elif d==6:
    #6. Ternary operator
    a=float(input("Enter a number: "))
    b=float(input("Enter another number: "))
    min=a if a<b else b
    print(min,"is the lowest number among the two numbers")

elif d==7:
    #7. Assignment operators
    a=float(input("Enter a number: "))
    a+=1
    print("Incrementing by 1:",a)
    a-=1
    print("Decrementing by 1:",a)
    a*=2
    print("Multiplying by 2:",a)
    a/=2
    print("Dividing by 2:",a)
    a%=2
    print("Remainder after dividing by 2:",a)
    a//=2
    print("Floor division by 2:",a)
    a**=2
    print("Square:",a)

elif d==8:
    #8. Bitwise operators
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    print('a&b:',a&b) #bitwise and operator
    print('a|b:',a|b) #bitwise or operator
    print('a^b:',a^b) #bitwise xor operator
    print('~a:', ~a) #bitwise negation operator
    print('~b:', ~b) #bitwise negation operator
    print('a<<b:',a<<b) #bitwise left shift operator
    print('a>>b:',a>>b) #bitwise right shift operator
else:
    print("Invalid operation!")





