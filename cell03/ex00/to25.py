#3.0
# รับข้อมูลจากผู้ใช้
a = int(input("Enter a number less than 25 : "))

# ตรวจสอบว่าเลขที่ใส่มานั้นถูกต้องหรือไม่
if a > 25:
    print("Error")
else:
    # บวกตัวเลขให้ถึง 25
    while a <= 25:
        print(f"Inside the loop, my variable is {a}")
        a += 1