# Напишете програма, която чете от конзолата следните три променливи, въведени от потребителя,
# и пресмята цената според цените от таблиците по-горе:
# •	плод  - banana / apple / orange / grapefruit / kiwi / pineapple / grapes;
# •	ден от седмицата  - Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday;
# •	количество (реално число).
# Резултатът да се отпечата закръглен с 2 цифри след десетичната точка.
# При невалиден ден от седмицата или невалидно име на плод да се отпечата "error". 






fruit = ["banana", "apple", "orange", "grapefruit", "kiwi", "pineapple", "grapes"]
workday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Satyrday", "Sunday"]

fruit_price = 0

fruit_choice = input("Enter a fruit: ")
day_choice = input("Choose a day: ")
amount = float(input("Enter the amount you want: "))

if fruit_choice in fruit and day_choice in workday and fruit_choice == fruit[0]:
    fruit_price = 2.50 * amount
    print(fruit_price)
elif fruit_choice in fruit and day_choice in workday and fruit_choice == fruit[1]:
    fruit_price = 1.20 * amount
    print(fruit_price)
elif fruit_choice in fruit and day_choice in workday and fruit_choice == fruit[2]:
    fruit_price = 0.85 * amount
    print(fruit_price)
elif fruit_choice in fruit and day_choice in workday and fruit_choice == fruit[3]:
    fruit_price = 1.45 * amount
    print(fruit_price)
elif fruit_choice in fruit and day_choice in workday and fruit_choice == fruit[4]:
    fruit_price = 2.70 * amount
    print(fruit_price)
elif fruit_choice in fruit and day_choice in workday and fruit_choice == fruit[5]:
    fruit_price= 5.50 * amount
    print(fruit_price)
elif fruit_choice in fruit and day_choice in workday and fruit_choice == fruit[6]:
    fruit_price = 3.85 * amount
    print(fruit_price)


if fruit_choice in fruit and day_choice in weekend and fruit_choice == fruit[0]:
    fruit_price = 2.70 * amount
    print(fruit_price)
elif fruit_choice in fruit and day_choice in weekend and fruit_choice == fruit[1]:
    fruit_price = 1.25 * amount
    print(fruit_price)
elif fruit_choice in fruit and day_choice in weekend and fruit_choice == fruit[2]:
    fruit_price = 0.90 * amount
    print(fruit_price)
elif fruit_choice in fruit and day_choice in weekend and fruit_choice == fruit[3]:
    fruit_price = 1.60 * amount
    print(fruit_price)
elif fruit_choice in fruit and day_choice in weekend and fruit_choice == fruit[4]:
    fruit_price = 3.00 * amount
    print(fruit_price)
elif fruit_choice in fruit and day_choice in weekend and fruit_choice == fruit[5]:
    fruit_price = 5.60 * amount
    print(fruit_price)
elif fruit_choice in fruit and day_choice in weekend and fruit_choice == fruit[6]:
    fruit_price = 4.20 * amount
    print(fruit_price)




