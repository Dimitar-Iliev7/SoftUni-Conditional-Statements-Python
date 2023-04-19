# 1.	Отлична оценка
# Първата задача от тази тема е да се напише конзолна програма,
# която чете оценка (реално число), въведена от потребителя и отпечатва "Excellent!",
# ако оценката е 5.50 или по-висока.


grade = float(input("What is the grade?"))

if grade < 3.50:
    print("poor")
elif grade > 3.50 and grade <= 4.50:
    print("not bad")
elif grade > 4.50 and grade < 5.50:
    print("almost there")
elif grade > 5.50:
    print("excellent")