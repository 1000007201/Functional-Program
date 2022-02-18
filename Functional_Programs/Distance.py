
def distance():
    x = int(input("Enter X Coordinate"))
    y = int(input("Enter Y Coordinate"))
    return (x**2 + y**2)**(1/2)


print(f"Distance:{distance()}")