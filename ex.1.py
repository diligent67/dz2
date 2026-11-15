with open("bigbob.txt", "w", encoding="utf-8") as bigbob:
    bigbob.write("Сегодня я учил ангем.\n")
    bigbob.write("Нифига не выучил.\n")
    bigbob.write("Как выучить 25 билет?.\n")
with open("bigbob.txt", "a", encoding="utf-8") as bigbob:
   bigbob.write("На некст неделе колоквиум\n")
with open("bigbob.txt", "r", encoding="utf-8") as bigbob:
    q = bigbob.readlines()
    k = len(q)
print("".join(q), end="")
print("Количество записей: ", k)