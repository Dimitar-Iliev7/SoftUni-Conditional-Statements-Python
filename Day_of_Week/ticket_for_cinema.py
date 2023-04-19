# 8.	Билет за кино
# Да се напише програма която чете ден от седмицата (текст) – 
# въведен от потребителя и принтира на конзолата цената на билет за кино според деня от седмицата:


day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
price = 0

day_to_watch = input("Which day do you want to visit? ")

if day_to_watch == day_of_week[0]:
    price += 12
    print(price)
elif day_to_watch == day_of_week[1]:
    price += 12
    print(price)
elif day_to_watch == day_of_week[2]:
    price += 14
    print(price)
elif day_to_watch == day_of_week[3]:
    price += 14
    print(price)
elif day_to_watch == day_of_week[4]:
    price += 12
    print(price)
elif day_to_watch == day_of_week[5]:
    price += 16
    print(price)
elif day_to_watch == day_of_week[6]:
    price += 16
    print(price)