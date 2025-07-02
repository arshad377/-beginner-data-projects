#Calculate Simple interest
def simple_interest():
    principal = float(input("enter the principal amount= "))
    rate = float(input("enter rate of interest= "))
    time = float(input("enter the time in years= "))
    simple_interest = (principal * rate * time) / 100
    

    print("simple interest={}".format(simple_interest))
    return simple_interest
simple_interest()
