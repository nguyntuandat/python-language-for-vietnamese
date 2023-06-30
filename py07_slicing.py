#7. SLICING
# #creat a substring by extracting elements from another string 
#           indexing[] or slice()
#           [start:stop:step]
#           (start,stop,step)
# tao mot chuoi bang cach chiet xuat phan tu cua mot chuoi khac
# start: bat dau, stop: ket thuc, step: so buoc

chuoigoc = "Nguyen Tuan Dat"

chuoiphu1 = chuoigoc[0:6]
chuoiphu2 = chuoigoc[7:11]
# chuoiphu3 in moi ki tu thu hai ke tu ki tu dau tien
chuoiphu3 = chuoigoc[0:15:2]
# chuoiphu 4 la in nguoc lai
chuoiphu4 = chuoigoc[::-1]

print(chuoiphu1)
print(chuoiphu2)
print(chuoiphu3)
print(chuoiphu4)

website1 = "http://google.com"
website2 = "http://facebook.com"

slice = slice(7,-4)

print(website1[slice])
print(website2[slice])