#Check whether the given year is leap year or not. If year is leap print ‘LEAP YEAR’ else
#print ‘COMMON YEAR’.
#Hint: • a year is a leap year if its number is exactly divisible by 4 and is not
#exactly divisible by 100
#• a year is always a leap year if its number is exactly divisible by 400

n = int(input("Enter a total days in year: "))
if (n // 4== 0 and n%100 == 0):
     print("The year is a leap year")
else:
    print("The yaer is not a leap year")



