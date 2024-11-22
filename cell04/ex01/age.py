# รับข้อมูลอายุปัจจุบันจากผู้ใช้
current_age = int(input("Please tell me your age: "))

# แสดงอายุในปัจจุบัน
print(f"You are currently {current_age} years old.")

# แสดงอายุในอีก 10, 20, และ 30 ปีข้างหน้า
for years in [10, 20, 30]:
    future_age = current_age + years
    print(f"In {years} years, you'll be {future_age} years old.")
