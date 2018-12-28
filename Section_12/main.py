from player import Player
from enemy import Enemy, Troll, Vampire, VampireKing

# tim = Player("Tim")

# print(tim.name)
# print(tim.lives)
# tim.lives -= 1
# print(tim.lives)

# Don't worry about getters and setters in Python, probably won't and don't need them!
# They can be useful, don't create them just for the sake of it however.

# print(tim.get_name())     # Getter
# tim.set_lives = 300       # Setter

# tim.lives -= 1
# print(tim)
# tim.lives -= 1
# print(tim)
# tim.lives -= 1
# print(tim)

# tim._lives = 9
# print(tim)

# tim.level = 2
# print(tim)
#
# tim.level += 5
# print(tim)
#
# tim.level -= 2
# print(tim)
#
# tim.score = 500
# print(tim)
#
# tim.level += 1
# print(tim)

# random_monster = Enemy("Basic Enemy", 12, 1)
# print(random_monster)
#
# random_monster.take_damage(4)
# print(random_monster)
#
# random_monster.take_damage(4)
# print(random_monster)
#
# random_monster.take_damage(4)
# print(random_monster)
#
# random_monster.take_damage(4)
# print(random_monster)

# print("=" * 80)
#
# ugly_troll = Troll("Pug")
# print("Ugly Troll - {}".format(ugly_troll))
#
# another_troll = Troll("Ug")
# print("Another Troll - {}".format(another_troll))
#
# brother = Troll("Urg")
# print(brother)
#
# # Python doesn't have overloaded methods, might be worth looking into for educational purposes
# # for example Troll(), Troll("Urg, 23), Troll("Ug", 18, 1) would all need different init methods in Java!
#
# ugly_troll.grunt()
# another_troll.grunt()
# brother.grunt()
#
# vamp_1 = Vampire("Mr. Vamp")
# print("First Vamp: {}".format(vamp_1))
#
# ugly_troll.take_damage(3)
# vamp_1.take_damage(2)
#
# # while vamp_1.alive:
# #     vamp_1.take_damage(1)
# #     print(vamp_1)
#
# vamp_1._lives = 0
# vamp_1._hit_points = 1
# print(vamp_1)
#
# print("=" * 50)
#
dracula = VampireKing("Dracula")
print(dracula)
dracula.take_damage(12)
print(dracula)

