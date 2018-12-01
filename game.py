# Game: Essence Quest
# Creator: Moro[CB4GANG]#9815 
# Date: November 30 2018
# Please do not steal, this is my first python project. :)
import time
import random
from user_stats import User, SilverSword, Fireball
from mob import Orc


def Begin():

    def Intro():
        dialogue = ["Old man: You have come far traveler.",
                    "Old man: What brings you so far from home?",
                    "You: I have come in search of Warlocks Essence.",
                    "Old man: Warlocks Essence?, my, my, my... You must be very worthy to obtain such an item."]
        for string in dialogue:
            print(string)
            time.sleep(0.8)

    Intro()

    def CharacterCreation():
        print("---------------------------")
        print("What is your name traveler?")
        name = input('>> ')
        print("So your name is {0}?".format(name))
        User.Name = name
        time.sleep(0.4)

    CharacterCreation()

    def PixieMeeting():
        dialogue = ["---------------------------",
                    "You start your quest in the Elven Plains.",
                    "You pick up your sword...but you hear something in the bushes.",
                    "What could it be?",
                    "It jumps out of the bush and startles you...you fall over.",
                    "It's just a harmless Pixie."]
        for string in dialogue:
            print(string)
            time.sleep(0.8)

    PixieMeeting()

    def FireballSpell():
        dialogue = ["---------------------------",
                    "The Pixie decides to give you a gift after she startled you.",
                    "She gives you the Fireball Spell.",
                    "+ NEW SPELL UNLOCKED: The Fireball Spell can do anywhere from 5-10 damage and cost 2-5 mana. +"]
        for string in dialogue:
            print(string)
            time.sleep(0.8)

    FireballSpell()

    def FireballTesting():
        dialogue = ["---------------------------",
                    "You try to use the Fireball Spell",
                    "It took " + str(Fireball.mana_usage) + " mana and done " + str(Fireball.attack_damage) + " damage...you also set a bush on fire.",
                    "While the Pixie is there she also tells you your current stats.",
                    "Your health is 100 and your mana is 50"]
        for string in dialogue:
            print(string)
            time.sleep(0.8)

    FireballTesting()

    def OrcAttack():
        dialogue = ["--------------------------",
                    "You come across an Orc!",
                    "The Orc has " + str(Orc.health) + " health and " + str(Orc.attack_damage) + " damage!",
                    "Do you wish to attack? Y/N"]
        for string in dialogue:
            print(string)
            time.sleep(0.8)

        if input('>> ') == "Y":
            User_total_damage = 0
            Orc_total_damage = 0
            orc_damage = 0
            human_damage = 0 
            while Orc.health > 0 or User.health > 0:
                User_total_damage += SilverSword.attack_damage
                print("%s: Silver Sword!" % User.Name)
                User_total_damage += Starfall.attack_damage
                print("%s: Star Fall!" % User.Name)
                Orc_total_damage += Orc.attack_damage
                print("Orc: Attack!")
                human_damage = User_total_damage
                orc_damage = Orc_total_damage
                Orc.health -= human_damage
                User.health -= orc_damage
                if Orc.health < User_total_damage:
                    print("Great! Orc Died")
                    break
                if User.health < Orc_total_damage:
                    print("Oh no %s Died", User.name)
                    break
                print("You done %i damage." % human_damage , " The Orc done %i damage." % orc_damage, "the Orc's health is now " + str(Orc.health) + ", %s's health is now " % str(User.name) + ".")
                orc_damage = 0
                human_damage = 0

            print("You've done %i damage" % User_total_damage + "\nThe Orc done %i damage\n" % Orc_total_damage + "%s's health: " % str(User.Name) + str(User.health) + ".")
           
    OrcAttack()


def TitleScreen():
    dialogue = ["    ______                                  ____                  __ ",
                "   / ____/____________  ____  ________     / __ \\__  _____  _____/ /_",
                "  / __/ / ___/ ___/ _ \\/ __ \\/ ___/ _ \\   / / / / / / / _ \\/ ___/ __/",
                " / /___(__  |__  )  __/ / / / /__/  __/  / /_/ / /_/ /  __(__  ) /_  ",
                "/_____/____/____/\\___/_/ /_/\\___/\\___/   \\___\\_\\__,_/\\___/____/\\__/  "]
    for string in dialogue:
        print(string)
        time.sleep(0.4)

    print("--------------------------")
    choice = input("WOULD YOU LIKE TO BEGIN YOUR JOURNEY? - Y/N >> ")
    if choice == 'Y':
        Begin()
    elif choice == 'N':
        quit()
    else:
        print("Invalid Option")
    print("--------------------------")


TitleScreen()
