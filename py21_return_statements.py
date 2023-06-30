#21. RETURN STATEMENTS
# functions send Python values/objects back to the caller.
# These values/objects are known as the function's return value
# lenh return = cac ham gui cac gia tri/ doi tuong trong python tro lai nguoi goi
# cac gia tri/ doi tuong nay duoc goi la gia tri tra ve cua ham

def multiply(number1,number2):
    result = number1 * number2
    return result

x = multiply(6,8)

print(x)