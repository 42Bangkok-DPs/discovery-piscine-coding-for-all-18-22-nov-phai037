def multiplication_table(number):
    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")

# กำหนดเลขแม่สูตรคูณที่ต้องการ
number = int(input("ENTER A NUMBER: "))
multiplication_table(number)
