#19. INDEX OPERATOR []
# gives access to a sequence's element (str,lists,tuples)
# cap quyen truy cap vao phan tu cua cac chuoi(str,list,tuples la cac chuoi)

ten_rieng = "nguyen Tuan Dat"

if (ten_rieng[0].islower()): #islower tuc la viet thuong
    ten_rieng = ten_rieng.capitalize()

ten_ho = ten_rieng[:6].upper() #upper la viet hoa toan bo, neu pham vi bat dau bang 0, co the bo so 0
ten_chinh = ten_rieng[7:].lower() # lower la viet thuong toan bo, neu pham vi ket thuc o cuoi cung cua chuoi, co the bo vi tri cuoi cung
last_character = ten_rieng[-1]

print(ten_rieng)
print(ten_ho)
print(ten_chinh)