# 9.	Плод или зеленчук
# Да се напише програма, която чете име на продукт, въведено от потребителя, и проверява дали е плод или зеленчук.


fruits = ["banana", "apple", "kiwi", "cherry", "lemon", "grapes"]
vegetables = ["tomato", "cucumber", "pepper", "carrot"]

user_choice = input("Enter a food: ")

if user_choice in fruits:
    print("fruits")
elif user_choice in vegetables:
    print("vegetables")
else:
    print("unknown")