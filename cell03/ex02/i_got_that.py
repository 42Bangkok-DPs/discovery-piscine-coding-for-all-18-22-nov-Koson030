#3.2
a = input("What you gotta say?: ") # รับข้อความแรกจากผู้ใช้

while True : # ลูปถามต่อไปจนกว่าจะพิมพ์ "STOP"
    b = input("I got that! else?: ")
    if b == "STOP":  # ถ้าพิมพ์ "STOP" จะหยุดลูป
        break