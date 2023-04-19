# Да се напише програма, която чете час от денонощието(цяло число) и ден от седмицата(текст)
# - въведени от потребителя и проверява дали офисът на фирма е отворен,
# като работното време на офисът е от 10-18 часа, от понеделник до събота включително

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
working_hours = [10, 11, 12, 13, 14, 15, 16, 17, 18]
rest_day = "Sunday"


check_the_time = int(input("Check if the time is working? "))
check_the_day = input("Which day do you want to come? ")

if check_the_time in working_hours and check_the_day in days:
    print("open")
elif check_the_time in working_hours and check_the_day in rest_day:
    print("closed")
else:
    print("closed")
