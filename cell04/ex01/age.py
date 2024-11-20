#4.1
# รับอายุจากผู้ใช้
a = int(input("Please tell me your age: "))
print(f"You are currently {a} years old.") # แสดงอายุเริ่มต้น

for years in range(10, 31, 10):  # range(10, 31, 10) จะทำการเพิ่ม 10 ปี ไปจนถึง 30 ปี
    future_age = a + years
    print(f"In {years} years, you'll be {future_age} years old.")

