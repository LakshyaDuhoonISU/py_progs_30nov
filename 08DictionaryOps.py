#dictionary operations
d={1:"hello","abc":2,45:34}
print(d)
print(d["abc"])
print(d[1])

d[1]="bye" #modifying a value of a key
print(d[1])

d[5]="bidnbovw" #adding a new key value pair
print(d)

del d[5] #deleting a key value pair
print(d)

d2=d.copy() #copy function copies a dictionary, therefore, d2 will have a copy of d
d[1]="hello" 
print(d)
print(d2) #d2 will have previous values of d
