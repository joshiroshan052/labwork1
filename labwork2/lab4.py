#the number should print two numbers: the number of hours between 0 and 23 and
# the number of minutes between 0 and 59
num = int(input("Enter a number: "))
hour = num // 60
minutes = num % 60
print(hour, minutes)

