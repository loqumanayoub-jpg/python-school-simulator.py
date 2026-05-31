class statistique:
    def __init__(self, data):
        self.data = data
        self. effectif = sum(data.values())

    def moyenne(self):
       total_points = 0
       total_effectif = 0
       for point, effectif in self.data.items():
        total_points += point * effectif
        total_effectif += effectif
       return total_points / total_effectif if total_effectif > 0 else 0

    def mediane(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        if n % 2 == 0:
            return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        else:
            return sorted_data[n // 2]

    def variance(self):
        mean = self.moyenne()
        return sum((x - mean) ** 2 for x in self.data) / len(self.data)

    def ecart_type(self):
        return self.variance() ** 0.5
# جدول نقط حقيقي (النقطة: عدد التلاميذ)
notes_classe = {10: 3, 12: 5, 15: 2}

# إنشاء كائن من الكلاس
mon_calcul = statistique(notes_classe)

# طباعة النتائج
print("الحصيص الإجمالي:", mon_calcul.effectif)
print("المعدل الحسابي:", mon_calcul.moyenne())

class fonctions:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def calculer_image(self, x):
        return self.a * x + self.b
    def type_de_fonction(self):
        if self.a == 0:
            return "ثابتة"
        else:
            return "خطية"
f1 = fonctions(2, 3)
print("نوع الدالة:", f1.type_de_fonction())
x = 5
print(f"صورة {x} في الدالة هي: {f1.calculer_image(x)}")
user_a = float(input("أدخل قيمة a: "))
user_b = float(input("أدخل قيمة b: "))
ma_fonction = fonctions(user_a, user_b)
print("نوع الدالة:", ma_fonction.type_de_fonction())
x = float(input("أدخل قيمة x: "))
print(f"صورة {x} في الدالة هي: {ma_fonction.calculer_image(x)}")
user_x = float(input("أدخل قيمة x: "))
print(f"صورة {user_x} في الدالة هي: {ma_fonction.calculer_image(user_x)}")