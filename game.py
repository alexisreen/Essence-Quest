# Game: Search for the draconic essence
# Creator: Lewis Murray (Anarchy)
# Date: November 30 2018
# Please do not steal, this is my first python project. :)
import time
import random
from user_stats import Fireball, User, SilverSword
from mob import Orc


def Begin():

    def Intro():
        dialogue = ["Old man: You have come far traveler.",
                    "Old man: What brings you so far from home?",
                    "You: I have come in search of draconic essence.",
                    "Old man: Draconic essence?, my, my, my... You must be very worthy to obtain such an item."]
        for string in dialogue:
            print(string)
            time.sleep(0.7)


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
            time.sleep(0.7)


    PixieMeeting()


    def FireballSpell():
        dialogue = ["---------------------------",
                    "The Pixie decides to give you a gift after she startled you.",
                    "She gives you the Fireball Spell.",
                    "+ NEW SPELL UNLOCKED: The Fireball Spell can do anywhere from 5-10 damage and cost 2-5 mana. +"]
        for string in dialogue:
            print(string)
            time.sleep(0.7)


    FireballSpell()


    def FireballTesting():
        dialogue = ["---------------------------",
                    "You try to use the Fireball Spell",
                    "It took " + str(Fireball.mana_usage) + " mana and done " + str(Fireball.attack_damage) + " damage...you also set a bush on fire.",
                    "While the Pixie is there she also tells you your current stats.",
                    "Your health is 100 and your mana is 50"]
        for string in dialogue:
            print(string)
            time.sleep(0.7)


    FireballTesting()


    def OrcAttack():
        dialogue = ["--------------------------",
                    "You come across an Orc!",
                    "The Orc has " + str(Orc.health) + " health and " + str(Orc.attack_damage) + " damage!",
                    "You're health is: %i" % User.health,
                    "Do you wish to attack? Y/N"]
        for string in dialogue:
            print(string)
            time.sleep(0.7)


        if input('>> ') == "Y":
            user_total_damage = 0
            orc_total_damage = 0
            while Orc.health > 5 or User.health > 0:
                user_total_damage += SilverSword.attack_damage
                orc_total_damage += Orc.attack_damage
                Orc.health -= SilverSword.attack_damage
                User.health -= Orc.attack_damage 
                if User.health < 60:
                    BoostUser.HealthManaBoost()
                print("Increased your health by: %i" % (User.health-orc_total_damage))
                if Orc.health < user_total_damage:
                    print("Great! Orc Died\n")
                    break
                if User.health < orc_total_damage:
                    print("Crap! %s Died\n", User.Name)
                    break
                print("You done "+str(user_total_damage)+" damage, the Orc's health is now "+str(Orc.health)+", %s's health is now "%str(User.Name) + str(User.health)+ ".")

            print("You've done %i damage"%user_total_damage+"\nThe Orc done %i damage\n" % orc_total_damage  + "%s's health: " % str(User.Name) + str(User.health) + ".")


    OrcAttack()

def TitleScreen():
    dialogue = ["  ___                  _      ___          _____ _          ___                       _      ___                        ",
                " / __| ___ __ _ _ _ __| |_   | __|__ _ _  |_   _| |_  ___  |   \\ _ _ __ _ __ ___ _ _ (_)__  | __|______ ___ _ _  __ ___ ",
                " \\__ \\/ -_) _` | '_/ _| ' \\  | _/ _ \\ '_|   | | | ' \\/ -_) | |) | '_/ _` / _/ _ \\ ' \\| / _| | _|(_-<_-</ -_) ' \\/ _/ -_)",
                " |___/\\___\\__,_|_| \\__|_||_| |_|\\___/_|     |_| |_||_\\___| |___/|_| \\__,_\\__\\___/_||_|_\\__| |___/__/__/\\___|_||_\\__\\___|"]
    for string in dialogue:
        print(string)
        time.sleep(0.4)

    print("--------------------------")
    choice = input("WOULD YOU LIKE TO BEGIN YOUR JOURNEY? - Y/N ")
    if choice == 'Y':
        Begin()
    elif choice == 'N':
        quit()
    else:
        print("Invalid Option")
    print("--------------------------")

TitleScreen()
