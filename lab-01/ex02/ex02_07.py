print("Nhap cac dong van ban (Nhap 'done' de ket thuc): ")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
print("\nCac dong da nhap sau da chuyen thanh in hoa: ")
for line in lines:
    print(line.upper())