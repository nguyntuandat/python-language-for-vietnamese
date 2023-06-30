#11. FOR LOOP
# a statement that will execute it's block of code a limited amount of times
# while loop = unlimited
# for loop = limited

import time

for i in range(10):
    print(i+1)

for i in range(1,11,2):
    print(i)

for i in "Nguyen Tuan Dat":
    print(i)

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("amogus")