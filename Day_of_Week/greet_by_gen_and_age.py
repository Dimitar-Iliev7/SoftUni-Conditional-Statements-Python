# 4.	Обръщение според възраст и пол
# Да се напише конзолна програма, която прочита възраст (реално число) и пол ('m' или 'f'),
# въведени от потребителя, и отпечатва обръщение измежду следните:
# •	"Mr." – мъж (пол 'm') на 16 или повече години
# •	"Master" – момче (пол 'm') под 16 години
# •	"Ms." – жена (пол 'f') на 16 или повече години
# •	"Miss" – момиче (пол 'f') под 16 години


age = float(input("enter age: "))
gender = input("enter gender, m ot f: ")

if gender == "m" and age < 16:
    print("Master")
elif gender == "m" and age >= 16:
    print("Mr.") 
elif gender == "f" and age < 16:
    print("Miss")
elif gender == "f" and age >= 16:
    print("Miss")