#Given three integers, print the smallest one. (Three integers should be user input)

a = int(input("Enter a first integer: "))
b = int(input("Enter a second integer: "))
c = int(input("Enter a third integer: "))
if(a<b<c):
    print("first integer is smallest one")
elif(b<a<c):
    print("second integer is smallest one")
else:
    print("third integer is smallest one")
    

