#13. LOOP CONTROL STATEMENTS
# change a loop execution from its normal sequence
# lenh de dieu khien vong lap

# break = used to terminate the loop entirely : duoc su dung de ket thuc hoan toan vong lap
# continue = skips to the next iteration of the loop : bo qua buoc lap tiep theo cua vong lap
# pass = does nothing, acts as a place holder : khong lam gi ca, dong vai tro giu cho

while True:
    ten = input("Enter your name: ")
    if ten != "":
        break
# ket thuc khi da go ten

phone_number = "0866-069-266"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")
# bo qua dau gach ngang

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)
# bo so 13