day=input("Enter day name here= ")
match day.capitalize():
    case "Monday"|"Tuesday"|"Wednesday"|"Thursday"|"Friday":
        print("{} is working day".format(day))
    case "Saturday":
        print("{} is week day".format(day))
    case "Sunday":
        print("{} is Holiday".format(day))
    case _:
        print("{} is not a day".format(day))
