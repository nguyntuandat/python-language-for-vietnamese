#22. KEYWORD ARGUMENTS
# arguments preceded by an identifier when we pass them to a function
# The older of the arguments doesn't matter, unlike positional arguments
# Python knows the names of the arguments that our function receives
# Cac doi so dung truoc mot ma dinh danh khi chung ta chuyen chung vao mot ham
# Doi so cu hon khong quan trong, khong giong nhu doi so vi tri
# Python biet ten cua cac doi so ma ham cua chung toi nhan duoc

def hello(dautien,thuhai,thuba):
    print("Hello "+dautien+" "+thuhai+" "+thuba)

hello(thuba="Dat",thuhai="Tuan",dautien="Nguyen")