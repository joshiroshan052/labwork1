#You live 4 miles form university.the bus drives at 25mph but spends 2 minutes at each of the 10 stops on the way.
#How long will the bus journey take?Alternatively, you could run to university. You jog the first mile at 7mph;then
#run the next two at 15mph; before jogging the last at 7mph again . We this be quicker or slower than the bus?

distance = 4
speed = 25
T1 = ((distance/speed)*60)
#Since the bus spend two mins and each 10 steps, so 2*10
T2 = 20
Total = T1 = T2
print(f"Total time taken by is:)
j1 = (1/7*60)
j2 = (1/15*60)
j3 = (1/7*60)
total = j1+j2+j3
print("Total jogging time is {}").format(total)
if Total>total:
    print("jogging is slower than bus")
else:
    print("jogging is faster than bus")

