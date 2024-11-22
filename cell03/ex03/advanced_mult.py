# สร้างตารางการคูณจาก 0 ถึง 10
for i in range(11):  # วนซ้ำตั้งแต่ 0 ถึง 10
    row = [i * j for j in range(11)]  # สร้างแต่ละแถวด้วยการคูณ i กับ 0-10
    print(f"Table de {i}: {' '.join(map(str, row))}")
