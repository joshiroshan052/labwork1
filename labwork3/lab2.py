#WAP which accepts marks of four subjects and display total marks, percentage and grade.
# Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail

a = int(input("Enter a first subject marks: "))
b = int(input("Enter a second subject marks: "))
c = int(input("Enter a third subject marks: "))
d = int(input("Enter a fourth subject marks: "))
Total_marks = a+b+c+d
print(Total_marks)
percentage = Total_marks/400*100
if percentage>70:
    print("You got distinction")
elif percentage>60:
    print("You got first distinction")
elif percentage>40:
    print("You are just passed")
else:
    print("You are failed,padhne gara babu")
    



