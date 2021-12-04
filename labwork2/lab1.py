#convert seconds to day,hours,minutes and seconds
s = int(input("Enter a second: "))
day = (((s/60)/60)/24)
print(f"total day for given seconds: {day} ")
hour = ((s/60)/60)
print(f"total hours or given seconds: {hour}")
minutes = (s/60)
print(f"total minutes for given seconds: {minutes}")

