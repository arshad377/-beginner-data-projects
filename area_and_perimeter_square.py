side=float(input("enter side= "))
if side<=0:
    print("{}".format(side))
else:
    area=side*side
    perimeter=4*side
    print("area of square=".format(area))
    print("perimeter of square=".format(perimeter))
