#26. **KWARGS 
# parameter that will pack all arguments into a dictionary
# useful so that a function can accept a varying amount of keyword argument

def xinchao(**kwargs):
    print("Hello " + kwargs['tenho'] + "" + kwargs['tenchinh'])
    print("Hello ", end=" ")            # end = " " de ngan xuong dong
    for key,value in kwargs.items():
        print(value,end=" ")

xinchao(danhxung="Mr.",tenho="Nguyen",tendem="Tuan",tenchinh="Dat")