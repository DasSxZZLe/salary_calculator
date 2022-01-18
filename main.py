hourly = input("Please enter your hourly salary: ")
daily = 8 * int(hourly)
monthly = daily * 20
yearly = monthly * 12

print("Your hourly salary is " + str(hourly) + "€")
print("You earn " + str(daily) + "€ a day!")
print("You earn " + str(monthly) + "€ on 20 Workdays (that's round about all workdays a month )!")
print("That means, that u earn " + str(yearly) + "€ per year(12 months)!")
print("")
input("Please press any key to close the salary calculator. Have a nice day: ")
