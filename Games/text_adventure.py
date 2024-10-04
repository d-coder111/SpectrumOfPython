import random

class Player:
    def __init__(self):
        self.health = 100
        self.attack_points = 10
        self.inventory = []

    def is_alive(self):
        return self.health > 0

    def add_item(self, item):
        self.inventory.append(item)

    def __str__(self):
        return f"Health: {self.health} ❤️, Attack Points: {self.attack_points} ⚔️, Inventory: {self.inventory}"

def intro():
    print("🏰 Welcome to the Text Adventure!")
    print("You find yourself in a dark dungeon with two paths ahead.")
    print("Choose wisely, as danger lurks around every corner. 🌌")

def choose_path():
    choice = input("Do you want to go left or right? (L/R): ").strip().lower()
    if choice == 'l':
        return 'left'
    elif choice == 'r':
        return 'right'
    else:
        print("❌ Invalid choice! Please choose 'L' or 'R'.")
        return choose_path()

def encounter_monster(player):
    print("👾 You encounter a wild monster!")
    monster_health = random.randint(20, 50)
    monster_attack = random.randint(5, 15)

    while player.is_alive() and monster_health > 0:
        action = input("Do you want to fight or run away? (Fight/Run): ").strip().lower()
        if action == 'fight':
            monster_health -= player.attack_points
            print(f"You attack the monster! Monster's health: {monster_health} 💥")
            if monster_health > 0:
                player.health -= monster_attack
                print(f"The monster attacks you! Your health: {player.health} ❤️")
        elif action == 'run':
            print("🏃‍♂️ You ran away safely!")
            return True
        else:
            print("❌ Invalid choice! You hesitated and the monster attacked you. Game over.")
            player.health = 0
            break

    if monster_health <= 0:
        print("🎉 You defeated the monster!")
        return True
    else:
        print("💔 You have been defeated. Game over.")
        return False

def find_treasure(player):
    treasure_amount = random.randint(50, 150)
    print(f"You find a treasure chest and gain {treasure_amount} gold coins! 💰")
    player.add_item(f"{treasure_amount} gold")

def encounter_trap(player):
    trap_damage = random.randint(10, 30)
    player.health -= trap_damage
    print(f"⚠️ You fell into a trap! You lost {trap_damage} health. Your health: {player.health} ❤️")

def encounter_ally(player):
    print("🤝 You meet a friendly ally who gives you a health potion!")
    player.add_item("Health Potion 🍷")
    print("You now have the following items:", player.inventory)

def play_game():
    player = Player()
    intro()
    
    while player.is_alive():
        path = choose_path()
        if path == 'left':
            encounter_choice = random.choice(['monster', 'trap'])
            if encounter_choice == 'monster':
                if encounter_monster(player):
                    find_treasure(player)
            else:
                encounter_trap(player)
        else:
            encounter_choice = random.choice(['treasure', 'ally'])
            if encounter_choice == 'treasure':
                find_treasure(player)
            else:
                encounter_ally(player)

        print(player)

        if player.is_alive():
            play_again = input("Do you want to continue exploring? (Y/N): ").strip().lower()
            if play_again != 'y':
                print("👋 Thanks for playing! Goodbye!")
                break
        else:
            print("💀 You have perished. Game over.")

if __name__ == "__main__":
    play_game()
