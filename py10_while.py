#10. WHILE LOOP
# a statement that will execute it's block of code, as long as it's condition remains true
# mot cau lenh se thuc thi lenh cua no mien la dieu kien cua no van dung

yrname = ""

while len(yrname) < 9:
    yrname = input("Nhap ten dang nhap cua ban (luu y bao gom 8 chu cai): ")

print("Welcome to League of Legend " + yrname)