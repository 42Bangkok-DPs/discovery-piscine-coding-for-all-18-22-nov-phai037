# รับค่าตัวเลขจากผู้ใช้
start_number = int(input("Enter a number: "))

# ตรวจสอบเงื่อนไข
if start_number > 25:
    print("Error")  # หากตัวเลขมากกว่า 25 แสดงข้อผิดพลาด
else:
    print(f"Displaying numbers from {start_number} to 25:")
    for num in range(start_number, 26):  # ใช้ range เพื่อแสดงตัวเลขจาก start_number ถึง 25
        print(num)  # แสดงตัวเลขทีละตัว
