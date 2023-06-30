#25. *ARGS 
# parameter that will pack all arguments into a tuple
# useful so that a function can accept a varying amount of arguments

def add(*tong):         # dat ten the nao cx dc, k dc thieu dau *
    sum = 0
    tong = list(tong)   # tuple khong the thay doi, nen can chuyen no thanh dang list
    tong[0] = 0         # thay the vi tri 0 = 0
    for i in tong:
        sum += i
    return sum

print(add(1,2,3,4,5,6))