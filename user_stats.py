import random

class User():
	health = 100
	mana = 50
	Name = ""

class Fireball():
	mana_usage = random.randint(10, 15)
	attack_damage = random.randint(10,15)

class SilverSword():
	mana_usage = 0
	attack_damage = random.randint(5, 30)

class BoostUser():
	def HeathManaBoost():
		User.health += 20
		User.mana += 10