# using match case operator
import sys
print("-"*100)
print("\tArithmatics")
print("-"*100)
print("\t1.Addition")
print("\t2.Subtraction")
print("\t3.Multiplication")
print("\t4.Division")
print("\t5.modulus")
print("\t6.exponentiation")
print("\t7.exit")
print("-"*100)
a=int(input("Enter your choice= "))
print("-"*100)
match(a):
    case 1:
        a=int(input("Enter value of a= "))
        b=int(input("Enter value of b= "))
        print("sum of {} and {}={}".format(a,b,a+b))
    case 2:
        a = int(input("Enter value of a= "))
        b = int(input("Enter value of b= "))
        print("sub of {} and {}={}".format(a, b,a-b))
    case 3:
        a = int(input("Enter value of a= "))
        b = int(input("Enter value of b= "))
        print("mul of {} and {}={}".format(a,b,a*b))
    case 4:
        a = int(input("Enter value of a= "))
        b = int(input("Enter value of b= "))
        print("div of {} and {}={}".format(a,b,a/b))
        print("floor div of {} and {}={}".format(a,b,a//b))
    case 5:
        a = int(input("Enter value of a= "))
        b = int(input("Enter value of b= "))
        print("mod of {} and {}={}".format(a,b,a%b))
    case 6:
        a = int(input("Enter value of a= "))
        b = int(input("Enter value of b= "))
        print("expon of {} and {}={}".format(a,b,a**b))
    case 7:
        sys.exit()
    case _:
        print("your choice is wrong plz try again!!")
