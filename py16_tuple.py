#16. TUPLE 
# collection which is ordered and unchangeable. Use to group together related data
# danh sach sap xep theo thu tu va khong the thay doi. dung de nhom cac du lieu lien quan lai voi nhau

student = ("Nguyen Tuan Dat",17,"male")

print(student.count("Nguyen Tuan Dat")) # dem so luong gia tri xuat hien trong tuple
print(student.index("male")) # tim vi tri cua gia tri xuat hien trong tuple

for x in student:
    print(x)
# dung vong lap de in gia tri cua tuple

if "Nguyen Tuan Dat" in student:
    print("Nguyen Tuan Dat is here")
# dung lenh if de kiem tra xem phan tu co o trong tuple hay khong