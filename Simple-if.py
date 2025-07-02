# simple if statement
a=int(input("Enter value of a= "))
b=int(input("Enter value of b= "))
if a>b:
    print("bigger({} and {})={}".format(a,b,a))
if b>a:
    print("bigger({} and {})={}".format(a,b,b))
if a==b:
    print("both are Equal")
