#12. NESTED LOOPS
# The "inner loop" will finish all of it's iterations before finishing one iteration of the "outer loop"
# vong lap long nhau : vong lap trong se hoan thanh tat ca cac lan lap cua no truoc khi ket thuc mot lan lap cua vong lap ngoai

hang = int(input("Co bao nhieu hang (rows): "))
cot = int(input("Co bao nhieu cot (columns): "))
bieutuong = input("Chon mot bieu tuong (symbol): ")

for i in range(hang):
    for j in range(cot):
        print(bieutuong, end="") #end="" co tac dung ngan viec xuong dong truoc khi xong mot vong lap
    print() #cai nay de xuong dong