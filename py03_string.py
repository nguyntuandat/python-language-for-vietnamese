#3. CAC LENH VOI STR

#len: length - chi do dai cua bien
#find : tim vi tri ki tu, ki tu dau tien o vi tri 0
#capitalize : viet hoa chu cai dau dong
#upper : viet hoa toan bo chu cai
#lower : viet thuong toan bo chu cai
#isdigit : tra ve True hoac False - neu str la mot chu cai hoac so thap phan thi tra ve False, neu str la mot so thi tra ve True
#isalpha : xem day co phai la chu cai ko? ket qua la True hoac False
#count : dem so luong ki tu co trong bien
#replace : thay the ki tu
#*3: chi don gian la x3 bien

name2 = "dat"

print(len(name2))
print(name2.find("a"))
print(name2.capitalize())
print(name2.upper())
print(name2.lower())
print(name2.isdigit())
print(name2.isalpha())
print(name2.count("a"))
print(name2.replace("a","e"))
print(name2*3)