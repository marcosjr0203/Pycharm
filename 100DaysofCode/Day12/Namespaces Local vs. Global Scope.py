# Scope
enemies = 1


def increase_enemies():
    enemies = 2
    print(f"Enemies inside function: {enemies}")


increase_enemies()
print(f"Enemies oustide function: {enemies}")


# Local Scope


def drink_potion():
    potion_strenght = 2  # Local Scope
    print(potion_strenght)

drink_potion()
#print(potion_strenght)  # Outside scope, will print an error.


# Global Scope
player_health = 10


def drink_potion():
    potion_strenght = 2
    print(player_health)  # As player health is a global scope it can be called from inside the function

drink_potion()
print(player_health)


#Python doesn't have Block Scope
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]  # Don't counts as local scope (while, if, for)
print(new_enemy)


def create_new_enemy():
    game_level = 3
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        newenemy = enemies[0]  # Counts as local scope (inside a function)


print(newenemy)  # Inaccessible

enemies = 1

# Modifying Global Scope
enemies = 0


def increase_enemies():
    enemies += 2  # inaccessible
    global enemies
    enemies += 2  # accessible, now
    print(f"Enemies inside function: {enemies}")


increase_enemies()
print(f"Enemies oustide function: {enemies}")


# Global Constants
PI = 3.1415  # Constant variables are usually written in uppercase.


def calc():
    PI
