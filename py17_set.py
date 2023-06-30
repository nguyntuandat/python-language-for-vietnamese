#17. SET
# collection which is unordered, unindexed. No duplicate values
# danh sach ma khong co thu tu, khong lap muc luc. Khong co gia tri lap lai.

utensils_dodung = {"fork","spoon","knife"}
dishes = {"bowl","plate","cup","knife"}

utensils_dodung.add("napkin")
utensils_dodung.remove("fork")
utensils_dodung.clear()
utensils_dodung.update(dishes) # cap nhat set nay vao set khac
dinner_table = utensils_dodung.union(dishes) # tao mot set moi trong do chua ca hai set tren

print(utensils_dodung.difference(dishes)) # so sanh su khac nhau giua hai set, nhung thu ma utensils co ma dishes khong co
print(utensils_dodung.intersection(dishes)) # tim diem giong nhau giua hai set

for x in dinner_table:
    print(x)
# neu co gia tri trung lap, lenh print se chi in mot gia tri