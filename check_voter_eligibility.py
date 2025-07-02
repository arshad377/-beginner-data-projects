age=int(input("Enter your age= "))
voter_id=True
if age<18:
    print("You are not eligible to vote")
elif age>18 and voter_id:
    print("you are eligible to vote")
