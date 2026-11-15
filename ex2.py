import csv
with open("purchases.csv", "w", newline="", encoding="utf-8-sig") as q:
    k = csv.writer(q, delimiter=";")
    k.writerow(["Товар", "Цена за штуку", "Количество"])
    k.writerow(["Тетрадь", "2,50", 4])
    k.writerow(["Ручка", "1,20", 3])
    k.writerow(["Папка", "4,00", 2])
    k.writerow(["Маркер", "3,30", 1])
c = 0
with open("purchases.csv", "r", newline="", encoding="utf-8-sig") as q:
    r = csv.DictReader(q, delimiter=";")
    for a in r:
        price = float(a["Цена за штуку"].replace(",", "."))
        ac = round(price * int(a["Количество"]), 2)
        c = round(c + ac, 2)
        print(dict(a), "Стоимость:", ac)
print("Общая сумма:", c)
