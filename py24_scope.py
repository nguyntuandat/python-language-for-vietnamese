#24. SCOPE
# The region that a variable is recognized
# A variable is only available from inside the region it is created
# A global and locally scoped versions of a variable can be created
# Khu vuc mot bien duoc nhan dang
# Mot bien chi kha dung tu ben trong khu vuc no duoc tao
# Co the tao phien ban toan cuc va cuc bo cua mot bien

ten_cua_tao = "Tuan Dat" # global scope (available inside & outside functions)
def display_name():
    ten_cua_tao = "Dat" # local scope (available only inside this function)
    print(ten_cua_tao)

display_name()       # Neu co san bien cuc bo thi khi chay ham se uu tien in bien cuc bo va bien bi gioi han trong han
print(ten_cua_tao)   # Day la bien ben ngoai, co san ca ngoai va trong ham