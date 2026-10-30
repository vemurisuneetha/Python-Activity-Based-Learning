# 53 - Food Waste Monitoring System
days = int(input("Enter number of days: "))

for i in range(days):
    prepared = int(input("Enter prepared meals: "))
    served = int(input("Enter served meals: "))
    leftover = prepared - served
    wastage = (leftover / prepared) * 100
    print("Leftover:", leftover, "Wastage %:", wastage)
    if wastage > 10:
        print("Day exceeds acceptable wastage limit")
    else:
        print("Within limit")