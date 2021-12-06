#Write a Python program to sum three given integers. However, if two or more values are
#equal sum will be zero.

a = int(input("Enter any integer: "))
b = int(input("Enter any integer: "))
c = int(input("Enter any integer: "))
if a ==b or a==c or b==c  :
    print("The sum is zero")
else:
    sum=a+b+c
    print(f"the sum is {sum}")