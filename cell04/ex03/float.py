#!/bin/env python3
#4.3

number = input("Give me a number: ")#รับข้อมูลจากผู้ใช้

try: #ตรวจสอบว่าเป็นเลขทศนิยมหรือไม่
    float_number = float(number) #แปลงค่าเป็น float เพื่อตรวจสอบว่าเป็นทศนิยม
    
    if float_number == int(float_number):  #ตรวจสอบว่าเป็นจำนวนเต็มหรือทศนิยม
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
    print("กรุณากรอกเลขที่ถูกต้อง.")
