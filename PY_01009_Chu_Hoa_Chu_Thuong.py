s = input()
hoa = 0
for i in s:
    if i == i.upper():
        hoa += 1

thuong = len(s) - hoa
print(s.lower() if thuong >= hoa else s.upper())