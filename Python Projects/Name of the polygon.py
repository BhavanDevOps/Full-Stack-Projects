given_number_of_sides=int(input())

if (given_number_of_sides<3):
    print("Not Polygon")
elif (given_number_of_sides==3):
    print("Triangle")
elif (given_number_of_sides==4):
    print("Quadrilateral")
elif (given_number_of_sides==5):
    print("Pentagon")
else:
    print("Big Polygon")