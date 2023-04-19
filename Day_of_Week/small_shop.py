# Предприемчив българин отваря квартални магазинчета в няколко града и продава на различни цени според града:
# град / продукт	coffee	water	beer	sweets	peanuts
# Sofia	0.50	0.80	1.20	1.45	1.60
# Plovdiv	0.40	0.70	1.15	1.30	1.50
# Varna	0.45	0.70	1.10	1.35	1.55
# Напишете програма, която чете продукт (текст), град (текст) и количество (десетично число),
# въведени от потребителя, и пресмята и отпечатва колко струва съответното количество от избрания продукт в посочения град. 







product = input("Enter the product: ")
city = input("Enter the city: ")
quantity = float(input("Enter the quantity: "))
price = 0

if city == "Sofia":
    if product == "coffee":
        price = quantity * 0.50
        print(price)
    elif product == "water":
        price = quantity * 0.80
        print(price)
    elif product == "beer":
        price = quantity * 1.20
        print(price)
    elif product == "sweets":
        price = quantity * 1.45
        print(price)
    elif product == "peanuts":
        price = quantity * 1.60
        print(price)

if city == "Varna":
    if product == "coffee":
        price = quantity * 0.45
        print(price)
    elif product == "water":
        price = quantity * 0.70
        print(price)
    elif product == "beer":
        price = quantity * 1.10
        print(price)
    elif product == "sweets":
        price = quantity * 1.35
        print(price)
    elif product == "peanuts":
        price = quantity * 1.55
        print(price)

if city == "Plovdiv":
    if product == "coffee":
        price = quantity * 0.40
        print(price)
    elif product == "water":
        price = quantity * 0.70
        print(price)
    elif product == "beer":
        price = quantity * 1.15
        print(price)
    elif product == "sweets":
        price = quantity * 1.30
        print(price)
    elif product == "peanuts":
        price = quantity * 1.50
        print(price)