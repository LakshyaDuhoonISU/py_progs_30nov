#list operations
x=[1,"hello",2]
y=x
print(x)
x[1]=15
print(y)
x.append(5)
print(y)

z=x.append(15)
print(z==None) #append operation returns a value None
print(z)

x=x+[9,10] #concatenating creates a new list with same name
#y=x
print(x)
x.append(9)
print(x)
print(y)

l1=[1]
l2=list(l1) #list function copies a list therefore, l2 will have list l1
l1[0]=22
print(l1)
print(l2) #l2 has the previous values of l1
