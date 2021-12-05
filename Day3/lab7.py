#Given a positive real number, print its fractional part.
import math
n = float(input("Enter a positive number: "))
x,y = math.modf(n)
print(x)
print(y)

