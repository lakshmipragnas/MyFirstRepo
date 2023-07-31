x=input("enter a string")
for i in x:
    print(i)

#print the ascii value of the elements
for i in x:
    print(i,ord(i))

#print the capitalized alphabets
for i in x:
    print(i,i.upper())

#to count length of a string
length=0
for i in x:
    length+=1
print("the length of a string",length)