import random

class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self, other):
        damage = random.randint(5, 10)
        other.hp -= damage
        print(f"{self.name} attacked {other.name} for {damage} damage!")

    def heal(self):
        #random healing amount
        heal_amount = random.randint(5, 10)
        #add to the current hp
        self.hp += heal_amount

        print(f"{self.name} healed for {heal_amount} HP!")

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

    #2 use input
    if choice == "1":
        player.attack(enemy)
    elif choice == "2":
        player.heal()
    else: 
        print("You panicked and missed your turn")

    #hp checker
    if enemy.hp<= 0:
        print("Victory! The goblin is defeated")
        break

    #enemy attacks a player
    enemy.attack(player)

    #check if player died
    if player.hp <= 0:
        print("Defeat, you ran out of HP and died")
        break
