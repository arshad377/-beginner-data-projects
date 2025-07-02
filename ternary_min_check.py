# find the smallest among two values and check for equality
a=int(input("enter value of a= "))
b=int(input("enter value of b= "))
res= a if a<b else b if b<a else "values are equal"
print("res={}".format(res))
