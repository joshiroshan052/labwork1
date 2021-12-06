#Ask user to enter age, gender ( M or F ) and then using following rules print their place of service.
#if employee is female, then she will work only in urban areas.
#if employee is a male and age is in between 20 to 40 then he may work in anywhere
#if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
#And any other input of age should print "ERROR".

a = int(input("Enter a age: "))
g = str(input("Enter a gender: "))
if g == "F" or g=="f":
    print("She will work only in urban areas")
elif (g == "M" or g == "m") and range(20,41):
    print("He may work in anywhere")
elif (g=="M" or g=="m") and range(40,61):
    print("He will work in urban areas only")
else:
    print("ERROR")



