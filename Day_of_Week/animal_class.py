# 3.	Клас животно
# Напишете програма, която отпечатва класа на животното според неговото име, въведено от потребителя.
# 1.	dog -> mammal
# 2.	crocodile, tortoise, snake -> reptile
# 3.	others -> unknown

mammal = ["dog", "cat"]
reptile = ["crocodile", "tortoise", "snake"]
others = ["unknown"]

check_animal = input("enter animal: ")

if check_animal in mammal:
    print("Mammal")
elif check_animal in reptile:
    print("reptile")
else:
    print(others[0])