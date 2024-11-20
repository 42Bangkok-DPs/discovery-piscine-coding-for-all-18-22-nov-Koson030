#4.3
#รับข้อมูลจากผู้ใช้
number = input("กรุณากรอกตัวเลข: ")

try: #ตรวจสอบว่าเป็นเลขทศนิยมหรือไม่
    float_number = float(number) #แปลงค่าเป็น float เพื่อตรวจสอบว่าเป็นทศนิยม
    
    if float_number == int(float_number):  #ตรวจสอบว่าเป็นจำนวนเต็มหรือทศนิยม
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
    print("กรุณากรอกเลขที่ถูกต้อง.")
