import random
from playsound import playsound
import pyglet
import time



player = pyglet.media.Player()
source1 = pyglet.media.load('C:\projects\python\Text_rpg\horest.wav', streaming=False)
source2 = pyglet.media.load('C:\projects\python\Text_rpg\pillage.wav', streaming=False)
source3 = pyglet.media.load('C:\projects\python\Text_rpg\pight.m4a', streaming=False)
source4 = pyglet.media.load('C:\projects\python\Text_rpg\won.mp3', streaming=False)
player.queue(source1)
player.queue(source2)
player.queue(source3)
player.queue(source2)
player.queue(source4)
class Game:
    def __init__(self, villian = None, sword = None, name = None, boy_str = None, boy_clever = None, boy_hp = None, boy_stamina = None, stock = None, quest = None, quest_rep = None):
        self.stock = stock
        self.boy_str = boy_str
        self.boy_clv = boy_clever
        self.boy_hp = boy_hp
        self.boy_stm = boy_stamina
        self.sword = sword
        self.name = name
        self.quest = quest
        self.quest_rep = quest_rep
        self.villian = villian

    def get_stock(self):
        self.stock = Character(stock_list)

    def get_villian(self):
        self.villian = Villian(villian_list)

    def get_weapon(self):
        self.weapon = Weapon(weapon_list)
    #START OF THE GAME

    def start(self):
        player.play()
        print("Welcome to the snowland, i am Creator, so lets begin! \n Controls: Boy(1); Girl(2).")
        time.sleep(1)
        mf = int(input("Girl or Boy: "))
        time.sleep(1)
        if mf == 1:
            print("What a strong clever boy!")
            time.sleep(1)
        elif mf == 2:
            print("What a pretty girl!")
            time.sleep(1)
        else:
            print("There is only 2 variants to choose!")
            return
        self.name = input("What's your name: ")
        time.sleep(1)
        print(f"Sup {self.name}")
        if mf == 1:
            self.get_stock()
            print(f"1.Boy strength = {self.stock.boy_str} \n 2.Boy clever = {self.stock.boy_clv} \n 3.Boy HP = {self.stock.boy_hp} \n 4.Boy stamina = {self.stock.boy_stm}. \n And your stock is {self.stock.stock} with a {self.stock.rep} reputation! ")
            time.sleep(1)
        if mf == 2:
            self.get_stock()
            print(f"1.Girl strength = {self.stock.girl_str} \n 2.Girl clever = {self.stock.girl_clv} \n 3.Girl HP = {self.stock.girl_hp} \n 4.Girl stamina = {self.stock.girl_stm}. \n And your stock is {self.stock.stock} with a {self.stock.rep} reputation! ")
            time.sleep(1)
        print("--Hey travaler, how are you?--")
        time.sleep(1)
        answer1 = int(input("1.Im doing well, where am i? \n 2.I dont wanna to talk with you.\n Your answer: "))
        time.sleep(1)
        if answer1 == 1:
            print(f"Im doing well, my name is {self.name}, where we are btw?")
            time.sleep(1)
            print("--We are in the Snowland, village called Sinji, go have a look and take some work, everyone is this kingdom are working.--")
            time.sleep(1)
            print("K i will go to the village")

            #VILLAGE

            player.next_source()
            print("--Hey traveler! Can you help with a work!--")
            time.sleep(1)
            answer_quest = int(input("1.Yes \n 2.No \n Answer: "))
            if answer_quest == 1:
                self.get_villian()
                print(f"--Oh thank you, can you help me with Killing {self.villian.villian}, if you complete it you will resieve 15 reputation--")
                time.sleep(1)
                print("Will you accept it?")
                time.sleep(1)
                answer_quest = int(input("1.Yes \n 2.No \n Answer: "))
            if answer_quest == 1:
                self.get_weapon()
                print(f"Ok, but first to all let me give you that {self.weapon.weapon}")
            elif answer_quest == 2:
                self.get_villian()
                print("Oh, but i have another work maybe you will accept it?")
                print(f"Have a look to this -  Kill {self.villian.villian}, you will reciece 15 reputation")
                answer_quest = int(input("1.Yes \n 2.No \n Answer: "))
                if answer_quest == 1:
                    self.get_weapon()
                    print(f"Ok, but first to all let me give you that {self.weapon.weapon}")
                if answer_quest == 2:
                    self.get_weapon()
                    print(f"Oh.. but take that {self.weapon.weapon}, it will help you in your adventure!")
                else:
                    print("I dont get it")

            #BOY FIGHT
            print(f"There {self.villian.villian} lets beat them!")
            if mf == 1:
                player.next_source()
                print(f"Your stats: \n Hp: {self.stock.boy_hp} \n Damage: {self.weapon.weapon_dd} \n \n Enemy stats : \n Hp: {self.villian.villian_hp}, \n Damage: {self.villian.villian_dd}")
                atack = int(input("1.Atack \n 2.Block \n Answer: "))
                if atack == 1:
                    while self.villian.villian_hp >= 0 and self.stock.boy_hp >=0:
                        self.villian.villian_hp -= self.weapon.weapon_dd + self.stock.boy_str
                        self.stock.boy_hp -= self.villian.villian_dd
                        self.stock.boy_stm -= 1.50
                        print(f"You atacked your enemy and his hp now = {self.villian.villian_hp}, and villian attacked you, your hp now is {self.stock.boy_hp}, your stamina is {self.stock.boy_stm}")
                elif atack == 2:
                    while self.villian.villian_hp >= 0 and self.stock.boy_hp >=0:
                        self.villian.villian_dd -= self.stock.boy_hp
                        self.villian.villian_hp -= 1.25
                        self.stock.boy_stm -= 1.50
                        print(f"You blocked the atack and your hp now = {self.stock.boy_hp}, your stamina is {self.stock.boy_stm}")
                if self.villian.villian_hp <= 0:
                    self.stock.rep += 15
                    print("Nice i got it, now lets go to the dealer!")
                    player.next_source()
                    time.sleep(1)
                    if self.stock.boy_clv >= 5:
                        print(f"Well done traveler!, maybe you will help me with this small problem, the banker issued me a check, but I dont know how to count, please help me, have a look! \n Chek: 34 + 56 + 728")
                        answer2 = int(input("Its: "))
                        if answer2 == 818:
                            self.stock.rep += 30
                            print("Thank you!")
                            time.sleep(3)
                            player.next_source()
                            print("------- Congrats, you completed the game! -------")
                            print(f" Your rep stats: {self.stock.rep}")
                            print(f"Character name - {self.name}")
                            if self.stock.rep <= 20:
                                print("Your end is - Slave")
                            elif self.stock.rep >= 21 and self.stock.rep <= 55:
                                print("Your end is - Farmer")
                            elif self.stock.rep >= 56:
                                print("Your end - Lord of Sinji!")
                        else:
                            time.sleep(3)
                            print("wrong")
                            player.next_source()
                            print("------- Congrats, you completed the game! -------")
                            print(f" Your rep stats: {self.stock.rep}")
                            print(f"Character name - {self.name}")
                            if self.stock.rep <= 20:
                                print("Your end is - Slave")
                            elif self.stock.rep >= 21 and self.stock.rep <= 55:
                                print("Your end is - Farmer")
                            elif self.stock.rep >= 56:
                                print("Your end - Lord of Sinji!")
                    elif self.stock.boy_clv <= 4:
                            time.sleep(3)
                            print(f"Well done")
                            player.next_source()
                            print("------- Congrats, you completed the game! -------")
                            print(f" Your rep stats: {self.stock.rep}")
                            print(f"Character name - {self.name}")
                            if self.stock.rep <= 20:
                                print("Your end is - Slave")
                            elif self.stock.rep >= 21 and self.stock.rep <= 55:
                                print("Your end is - Farmer")
                            elif self.stock.rep >= 56:
                                print("Your end - Lord of Sinji!")
                elif self.stock.boy_hp <= 0:
                    player.pause()
                    print("You died!")
                elif self.stock.boy_stm <= 0:
                    player.pause()
                    print("You died!")

            #GIRL FIGHT
            if mf == 2:
                player.next_source()
                print(f"Your stats: \n Hp: {self.stock.girl_hp} \n Damage: {self.weapon.weapon_dd} \n \n Enemy stats : \n Hp: {self.villian.villian_hp}, \n Damage: {self.villian.villian_dd}")
                atack = int(input("1.Atack \n 2.Block \n Answer: "))
                if atack == 1:
                    while self.villian.villian_hp >= 0 and self.stock.girl_hp >=0:
                        self.villian.villian_hp -= self.weapon.weapon_dd + self.stock.girl_str
                        self.stock.girl_hp -= self.villian.villian_dd
                        self.stock.girl_stm -= 1.50
                        print(f"You atacked your enemy and his hp now = {self.villian.villian_hp}, and villian attacked you, your hp now is {self.stock.girl_hp}, your stamina is {self.stock.girl_stm}")
                elif atack == 2:
                    while self.villian.villian_hp >= 0 and self.stock.boy_hp >=0:
                        self.villian.villian_dd -= self.stock.girl_hp
                        print(f"You blocked the atack and your hp now = {self.stock.girl_hp}, your stamina is {self.stock.girl_stm}")
                if self.villian.villian_hp <= 0 and self.stock.girl_stm >= 0:
                    self.stock.rep += 15
                    print("Nice i got it, now lets go to the dealer!")
                    player.next_source()
                    time.sleep(1)
                    if self.stock.girl_clv >= 5:
                        print(f"Well done traveler, maybe you will help me with this small problem, the banker issued me a check, but I dont know how to count, please help me, have a look! \n Chek: 34 + 56 + 728")
                        answer2 = int(input("Its: "))
                        if answer2 == 818:
                            self.stock.rep += 30
                            self.final_rep = self.stock.rep
                            print("Thank you!")
                            time.sleep(3)
                            player.next_source()
                            print("------- Congrats, you completed the game! -------")
                            print(f" Your rep stats: {self.final_rep}")
                            print(f"Character name - {self.name}")
                            if self.stock.rep <= 20:
                                print("Your end is - Slave")
                            elif self.stock.rep >= 21 and self.stock.rep <= 55:
                                print("Your end is - Farmer")
                            elif self.stock.rep >= 56:
                                print("Your end - Lord of Sinji!")
                        else:
                            time.sleep(3)
                            self.final_rep = self.stock.rep
                            print("wrong")
                            player.next_source()
                            print("------- Congrats, you completed the game! -------")
                            print(f" Your rep stats: {self.final_rep}")
                            print(f"Character name - {self.name}")
                            if self.stock.rep <= 20:
                                print("Your end is - Slave")
                            elif self.stock.rep >= 21 and self.stock.rep <= 55:
                                print("Your end is - Farmer")
                            elif self.stock.rep >= 56:
                                print("Your end - Lord of Sinji!")
                    elif self.stock.girl_clv <= 4:
                            time.sleep(3)
                            player.next_source()
                            self.final_rep = self.stock.rep
                            print(f"Well done")
                            print("------- Congrats, you completed the game! -------")
                            print(f" Your rep stats: {self.final_rep}")
                            print(f"Character name - {self.name}")
                            if self.stock.rep <= 20:
                                print("Your end is - Slave")
                            elif self.stock.rep >= 21 and self.stock.rep <= 55:
                                print("Your end is - Farmer")
                            elif self.stock.rep >= 56:
                                print("Your end - Lord of Sinji!")
                elif self.stock.girl_hp <= 0:
                    player.pause()
                    print("You died!")
                elif self.stock.girl_stm <= 0:
                    player.pause()
                    print("You died!")

        #LOSE

        elif answer1 == 2:
            print(f"Get over here!")
            print("Oh, ok ok!")
class Character(Game):
    def __init__(self, stock_list):
        #boy
        self.stock = random.choice(list(stock_list))
        self.boy_str = random.randint(1,10)
        self.boy_clv = random.randint(1,10)
        self.boy_hp = random.randint(50,100)
        self.boy_stm = random.randint(50,100)
        self.rep = random.randint(14, 50)
        #girl
        self.girl_str = random.randint(1,10)
        self.girl_clv = random.randint(1,10)
        self.girl_hp = random.randint(50,100)
        self.girl_stm = random.randint(50,100)
stock_list = {
    "Orc",
    "Elf",
    "Dark Elf",
    "Human"
}


class Villian(Game):
    def __init__(self, villian_list):
        self.villian = random.choice(list(villian_list))
        self.villian_hp = villian_list[self.villian]["villian_hp"]
        self.villian_dd = villian_list[self.villian]["villian_dd"]
villian_list = {
    "Spider":
    {"villian_hp": 18, 
     "villian_dd": 6},
    "Slime":
    {"villian_hp": 20, 
     "villian_dd": 3},
    "Zombie":
    {"villian_hp": 40, 
     "villian_dd": 5},
    "Sheep":
    {"villian_hp": 10, 
     "villian_dd": 2},
}


class Weapon(Game):
    def __init__(self, weapon_list):
        self.weapon = random.choice(list(weapon_list))
        self.weapon_dd = weapon_list[self.weapon]["weapon_dd"]
weapon_list = {
    "Sword":
    {"weapon_dd": 5},
    "Bow":
    {"weapon_dd": 7},
    "Axe":
    {"weapon_dd": 3},
    "Pickaxe":
    {"weapon_dd": 2}
}


start1 = Game()
start1.start()
pyglet.app.run()