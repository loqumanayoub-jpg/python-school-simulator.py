from time import time


class teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def introduce(self):
        print(f"مرحبًا، أنا {self.name} وأدرس {self.subject}.")
teacher1 = teacher("أستاذ أحمد", "الرياضيات")
teacher2 = teacher("أستاذة ليلى", "العلوم")
teacher1.introduce()
teacher2.introduce()
class student:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

    def display_info(self):
        print(f"الطالب: {self.name}, الطاقة: {self.energy}")

    def study(self, hours):
        self.energy -= hours * 20
        print(f"{self.name} درس لمدة {hours} ساعة. الطاقة المتبقية: {self.energy}")

    def rest(self):
        self.energy += 10
        print(f"{self.name} استرقد. الطاقة المتبقية: {self.energy}")
        if self.energy > 100:
            self.energy = 100
            print(f"{self.name} طاقته ممتلئة الآن.")
class classroom:
    def __init__(self, teacher_list, students):
        self.teacher_list = teacher_list
        self.students = students

    def start_class(self):
        heure = 1
        for t in self.teacher_list:
            print(f" time {heure}: دخول {t.name} ليدرس{t.subject}.")
            for s in self.students:
                s.study(1)
            heure += 1
            if heure == 3:
                print("استراحة لمدة 15 دقيقة.")
                for s in self.students:
                    s.rest()
            if heure == 4:
                print("انتهت الحصة الدراسية.")
                break
        print("الطلاب الحاضرون:")
        for student in self.students:
            print(f"- {student.name} (طاقة: {student.energy})")
list_of_students = ["علي", "سارة", "محمد", "فاطمة"]
students = [student(name, 100) for name in list_of_students]
classroom1 = classroom([teacher1, teacher2], students)
classroom1.start_class()
while True:
    print("هل تريد بدء حصة دراسية جديدة؟ (نعم/لا)")
    answer = input().strip().lower()
    if answer == "نعم":
        classroom1.start_class()
    elif answer == "لا":
        print("شكراً لاستخدام برنامج الحصص الدراسية. إلى اللقاء!")
        break
    else:
        print("الرجاء إدخال 'نعم' أو 'لا'.")
