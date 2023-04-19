# 1.	Ден от седмицата
# Напишете програма, която чете цяло число, въведено от потребителя,
# и отпечатва ден от седмицата (на английски език),
# в граници [1...7] или отпечатва "Error" в случай, че въведеното число е невалидно. 


day = int(input("Enter a number: "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("error")