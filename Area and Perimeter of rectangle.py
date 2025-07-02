try:
 Length=float(input("length of rectangle:"))
 Breadth=float(input("breadth of rectangle:"))
 Area=Length*Breadth
 peri=2×(Length+Breadth)
 print("Area of rectangle:{}".format(Area))
except ValueError:
     print("Don't enter str/symbol or alpha-numeric")
