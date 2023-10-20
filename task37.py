month = input("Enter the month: ")

spring_months = ["January", "February", "March", "April", "May"]
summer_months = ["June", "July", "August"]
fall_months = ["September", "October", "November"]

if month in spring_months:
    print("Spring")
elif month in summer_months:
    print("Summer")
elif month in fall_months:
    print("Fall")
elif month == "December":
    print("Winter")
else:
    print("Invalid month")