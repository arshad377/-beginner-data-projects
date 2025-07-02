import sys

print("-"*50)
print("\tArea operations")
print("-"*50)
print("\tR.Rectangle")
print("\tS.Square")
print("\tC.circle")
print("\tT.Triangle")
print("\tE.exit")
print("-"*50)
select=input("Enter your choice= ")
select=select.upper()
print("-"*50)
match select:
    case "R":
        l=float(input("Enter length of rectangle= "))
        b=float(input("Enter breadth of rectangle= "))
        print("area of rectangle={}".format(l*b))
    case "S":
        side=float(input("Enter side of Square= "))
        print("area of square={}".format(side**2))
    case "C":
        r=float(input("Enter radius of circle= "))
        pi=3.14
        print("area of circle={}".format(pi*r**2))
    case "T":
        b=float(input("Enter breadth of triangle= "))
        h=float(input("Enter height of triangle= "))
        print("Area of triangle={}".format((1/2)*b*h))
    case "E":
        print("Thanks for using this program")
        sys.exit()
    case _:
        print("your choice is wrong try again!!")
