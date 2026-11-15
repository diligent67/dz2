import json
with open("participant.json", "w", encoding="utf-8") as file:
    json.dump({"Имя": "Алексей","Группа": "КБ-101","Навыки": ["Python", "Excel"],"Уведомления": True }, file, ensure_ascii=False, indent=4)
with open("participant.json", "r+", encoding="utf-8") as file:
    q= json.load(file)
    q["Навыки"] = q["Навыки"] + ["CSV"]
    q["Уведомления"] = not q["Уведомления"]
    file.seek(0)
    json.dump(q, file, ensure_ascii=False, indent=4)
with open("participant.json", "r", encoding="utf-8") as file:
    fq= json.load(file)
    print(f"Имя: {fq['Имя']}\nГруппа: {fq['Группа']}\nНавыки: {fq['Навыки']}\nУведомления: {fq['Уведомления']}")
