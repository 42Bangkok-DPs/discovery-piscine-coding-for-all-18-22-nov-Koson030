#4.2
# รับค่าอินพุตจากผู้ใช้และแปลงเป็นจำนวนเต็ม
a = int(input("Give me the first number: "))
b = int(input("Give me the second number: "))
print("Thank you!")

print(f"{a} + {b} = {a+b}") #แสดงผลการบวกของ a และ b
print(f"{a} - {b} = {a-b}") #แสดงผลการลบของ a และ b
print(f"{a} / {b} = {a//b}") #แสดงผลการหารของ a และ b โดยใช้การหารแบบปัดเศษลง (floor division)
print(f"{a} * {b} = {a*b}") #แสดงผลการคูณของ a และ b