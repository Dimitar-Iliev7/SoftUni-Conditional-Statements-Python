# 6.	Информация за скоростта
# Да се напише програма, която чете скорост (реално число), въведена от потребителя и отпечатва информация за скоростта. 
# •	При скорост до 10 (включително) отпечатайте "slow"
# •	При скорост над 10 и до 50 (включително) отпечатайте "average" 
# •	При скорост над 50 и до 150 (включително) отпечатайте "fast"
# •	При скорост над 150 и до 1000 (включително) отпечатайте "ultra fast" 
# •	При по-висока скорост отпечатайте "extremely fast"


speed = float(input("What is the speed: "))

if speed <= 10:
    print("slow")
elif speed > 10 and speed <= 50:
    print("average")
elif speed > 50 and speed <= 150:
    print("fast")
elif speed > 150 and speed <= 1000:
    print("ultra fast")
else:
    print("Extremely fast")