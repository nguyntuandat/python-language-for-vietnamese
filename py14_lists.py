#14. LISTS 
# used to store multiple items in a single variable

food = ["pizza","hamburger","hotdog","spaghetti"]
food[0] = "sushi" #thay the pizza = sushi

print(food)

food.append("ice cream") # them mot phan tu vao list
food.remove("hotdog") # xoa mot phan tu cua list
food.pop() # xoa phan tu cuoi cung
food.insert(0,"cake") # chen gia tri ma khong xoa
food.sort() # sap xep theo bang chu cai cac phan tu
food.clear() # xoa het cac phan tu

for x in food:
    print(x)