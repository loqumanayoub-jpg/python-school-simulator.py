tasks = []
tasks.append(float(input("المادة الأولى: ")))
tasks.append(float(input("المادة الثانية: ")))
tasks.append(float(input("المادة الثالثة: ")))
print("المجموع: ", sum(tasks)/3)
if sum(tasks)/3 >= 20:
    print("جيد جدا جداً")
    result = sum(tasks)/3
elif sum(tasks)/3 >= 18:
    print("جيد جداً")
    result = sum(tasks)/3
elif sum(tasks)/3 >= 16:
    print("حسناً")
    result = sum(tasks)/3
elif sum(tasks)/3 >= 14:
    print("مستحسن")
    result = sum(tasks)/3
elif sum(tasks)/3 >= 12:
    print("مقبول")
    result = sum(tasks)/3
elif sum(tasks)/3 >= 10:
    print("ضعيف")
    result = sum(tasks)/3
else:
    print("ضعيف جداً")
    result = sum(tasks)/3
    