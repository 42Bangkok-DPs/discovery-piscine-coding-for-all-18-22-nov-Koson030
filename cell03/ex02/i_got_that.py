#3.2
while True:
    user_input = input("What you gotta say? : ")   # รับข้อความจากคีบอร์ด
    if user_input == "STOP": # ตรวจสอบว่าป้อน "STOP" หรือไม่
        break  # ออกจากลูปเมื่อพิมพ์ STOP
    print(f"I got that! Anything else? : {user_input}")  # แสดงข้อความตอบกลับเมื่อใส่คำที่ไม่ใช่stop

