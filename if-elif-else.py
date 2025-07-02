# program to find the biggest of 4 number
a=int(input("Enter value of a= "))
b=int(input("Enter value of b= "))
c=int(input("Enter value of c= "))
d=int(input("Enter value of d= "))

if a>=b and a>c and a>d:
    print("{} is Biggest".format(a))
elif b>=c and b>d and b>a:
    print("{} is Biggest".format(b))
elif c>=d and c>b and c>a:
    print("{} is Biggest".format(c))
elif d>=a and d>b and d>c:
    print("{} is Biggest".format(d))
else:
    print("All are Equal")
