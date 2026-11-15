with open("diary.txt", "w", encoding="utf-8") as diary:
    diary.write("Сегодня мы работали с файлами Python.\n")
    diary.write("Научились сохранять текст.\n")
    diary.write("Узнали, как читать данные обратно.\n")
with open("diary.txt", "a", encoding="utf-8") as diary:
   diary.write("Следующее занятие – CSV и JSON\n")
with open("diary.txt", "r", encoding="utf-8") as diary:
    q = diary.readlines()
    k = len(q)
print("".join(q), end="")
print("Количество записей: ", k)
