#A student will not be allowed to sit in exam if his/her attendence is less than 75%.
#Take following input from user
#Number of classes held
#Number of classes attended.
#And print
#percentage of class attended
#Is student is allowed to sit in exam or not.

c = int(input("Enter a classes held: "))
ca = int(input("Enter a classes attended: "))
percentage_of_class_attend = c/ca*100
if percentage_of_class_attend > 75:
    print("He/she can sit in exam")
else:
    print("He/she cannot sit in exam")
