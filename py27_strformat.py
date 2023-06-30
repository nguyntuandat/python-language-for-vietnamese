#27. STR.FORMAT() 
# optional method that gives users more control when displaying output
# phuong phap tuy chon cho phep nguoi dung kiem soat nhieu hon khi hien thi dau ra

animal = "cow"
item = "moon"

#print("The {} jumped over the {}".format(animal,item))
#print("The {1} jumped over the {1}".format(animal,item)) # positional argument # {1} la vi tri
#print("The {animal} jumped over the {item}".format(animal="cow",item="moon"))  #keyword argument

text = "The {} jumped over the {}"
print(text.format(animal,item))

ten_tao = "Nguyen Tuan Dat"

print("Hello, my name is {}".format(ten_tao))
print("Hello, my name is {:<30}. Nice to meet you".format(ten_tao)) #:<30 can lech phai
print("Hello, my name is {:>30}. Nice to meet you".format(ten_tao)) #:>30 can lech trai
print("Hello, my name is {:^30}. Nice to meet you".format(ten_tao)) #:^30 can hai ben