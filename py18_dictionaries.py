#18. DICTIONARIES
# a changeable, unordered collection of unique (key: value) pairs 
# fast because they use hashing, allow us to access a value quickly
# danh sach co the thay doi, khong co thu tu chua cac cap (key:value)
# cho phep truy cap mot gia tri nhanh chong

# dictionary = {'key':'values'}
capitals = {'USA':'Washington DC',
            'India':'New Delhi',
            'China':'Beijing',
            'Viet Nam':'Ha Noi',
            'Russia':'Moscow'}

capitals.update({'Germany':'Berlin'}) # update cap gia tri moi
capitals.update({'USA':'Las Vegas'}) # update values moi cho mot key nhat dinh
capitals.pop('China') # xoa mot cap gia tri
capitals.clear() # xoa toan bo cap gia tri

print(capitals['Russia'])
print(capitals.get('Germany')) # kiem tra xem Germany co trong danh sach khong
print(capitals.keys()) # in toan bo key cua Dictionary
print(capitals.values()) # in toan bo values cua Dictionary
print(capitals.items()) # in toan bo gia tri

for key,value in capitals.items():
    print(key, value)
# dung vong lap de hien thi cac cap gia tri