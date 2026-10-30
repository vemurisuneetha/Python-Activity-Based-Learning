# 51 - Bus Passenger Occupancy Simulation
capacity = 40
passengers = 0
stops = int(input("Enter number of stops: "))

for i in range(1, stops+1):
    board = int(input(f"Stop {i} boarding: "))
    alight = int(input(f"Stop {i} alighting: "))
    passengers = passengers + board - alight
    print("Current passengers:", passengers)
    if passengers > capacity:
        print("Bus Overloaded - Capacity Violation")
    if passengers < 0:
        passengers = 0