#TASK 1

class Ingradients:
    potato = "Potatoes"
    sugar_beet = "Nice red beet"
    cabbage = "Green cabbage"
    tomatoes = "Sweet tomatoes"
    meat = "Beef"

class Pan(Ingradients):
    water = "Hot boiled water"
    flavours = "Pepper and salt"

class Borsh(Pan):
    def __init__(self):
        print(f"Hello, its Gordon Ramsay, and today we will make a Ukranian traditional food called 'Borsch' \n first to all put a {self.water}, flavours: {self.flavours} and add {self.meat} to a pan to make a bouillon. \n than add {self.potato}, {self.sugar_beet},{self.cabbage} and {self.tomatoes} \n enjoy your meal!")

food = Borsh()

#TASK2

import random
def coding():
    __1st = int(input("First number: "))
    __2nd = int(input("Second number: "))

    for i in range(2):
        code = random.randint(1,5)
        if code == 1:
            code_1 = __1st + __2nd
            print(f"Your code is {code_1}")
        if code == 2:
            code_2 = __1st - __2nd
            print(f"Your code is {code_2}")
        if code == 3:
            code_3 = __1st * __2nd
            print(f"Your code is {code_3}")
        if code == 4:
            code_4 = __1st // __2nd
            print(f"Your code is {code_4}")
        if code == 5:
            code_5 = __1st ** __2nd
            print(f"Your code is {code_5}")
math_code = coding()