import random

# break = destroy the loop and move to the next block of code (outside of loop)
# continue = skip the rest of current loop, and go back to the start of loop
# pass = does nothing but correctly close off the syntax so no error



class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.max_hp = hp #save the originally set HP as the max_hp
        self.potions = 3 #potions default to 3

    def attack(self, other):
        damage = random.randint(5, 10)
        other.hp -= damage
        print(f"{self.name} attacked {other.name} for {damage} damage!")

    def heal(self):

        if self.potions > 0:
            #random healing amount
            heal_amount = random.randint(5, 10)
            #add to the current hp
            self.hp += heal_amount

            if self.hp > self.max_hp:
                self.hp = self.max_hp

            #remove one used potion from inventory
            self.potions -= 1

            
            print(f"{self.name} used a potion and healed for {heal_amount} HP! (Current HP: {self.hp}/{self.max_hp})")
            print(f"You used a potion, number of potions remaining: {self.potions}")
            return True
        
        else:
            print("You reach for a potion but your bag is empty!")
            return False
        
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
        #only let enemy attack if the heal was successful 
        if player.heal():
            pass #the turn happened 
        else: 
            continue
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
