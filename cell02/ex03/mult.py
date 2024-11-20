#2.3
# รับค่าจากผู้ใช้
a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

# คูณและแสดงผล
x = a * b

# ตรวจสอบผลลัพธ์
print(f"{a} x {b} = {x}")
if x > 0 :
    print("The result is positive.")
elif x < 0 :
    print("The result is negative.")
elif x == 0 :
    print("The result is positive and negative")