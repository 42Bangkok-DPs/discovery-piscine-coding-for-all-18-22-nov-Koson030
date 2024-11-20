#2.2
# กำหนดรหัสผ่านที่ถูกต้อง
password = "Python is awesome"

# ขอให้ผู้ใช้ป้อนรหัสผ่าน
password1 = input("Please enter your password: ")

# ตรวจสอบรหัสผ่านที่ผู้ใช้ป้อน
if password1 == password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")
