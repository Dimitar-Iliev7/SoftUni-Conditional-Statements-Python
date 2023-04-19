# 2.	Почивен или работен ден
# Напишете програма която, чете ден от седмицата (текст), на английски език 
# - въведен от потребителя.Ако денят е работен отпечатва на конзолата 
# - "Working day", ако е почивен - "Weekend". Ако се въведе текст различен от ден от седмицата
# да се отпечата - "Error".


working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
rest_days = ["Saturday", "Sunday"]

check = input("Enter a day: ")

if check in working_days:
    print("Working day")
elif check in rest_days:
    print("rest day")
else:
    print("Error")