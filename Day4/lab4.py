#Write a program to print absolute value of a number entered by user. E.g.-
#INPUT: 1        OUTPUT: 1
#INPUT: -1        OUTPUT: 1

a = int(input("Enter a value: "))
if a < 0:
    print(a* -1)
else:
    print(a)

