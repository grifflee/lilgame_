import random

class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self, other):
        damage = random.randint(5, 10)
        other.hp -= damage
        print(f"{self.name} attacked {other.name} for {damage} damage!")

#initalize the two characters
player = Character ("Hero", 100)
enemy = Character ("Goblin", 100)

#the game loop
while player.hp > 0 and enemy.hp > 0:

    #prints out the basic stats
    print(f"\n{player.name} HP: {player.hp} | {enemy.name} HP: {enemy.hp}")
    print("1. Attack")
    print("2. Heal")

    #Ask the user for their decision
    choice = input("Your move (1/2): ")