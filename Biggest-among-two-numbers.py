# find the biggest among 2 number
try:
    a=int(input("Enter value of a= "))
    b=int(input("enter value of b= "))

    if a>b:
        print("bigger({} and {})={}".format(a,b,a))
    else:
        if b>a:
            print("bigger({} and {})={}".format(a,b,b))
        else:
            print("Both are Equal")
except ValueError:
    print("plz don't use Special char or alpha numeric value")
