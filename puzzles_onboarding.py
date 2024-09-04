'''Your program must destroy the enemy ships by shooting the closest enemy on each turn.
  Rules
On each start of turn (within the game loop), you obtain information on the two closest enemies:

    enemy1 and dist1: the name and the distance to enemy 1.
    enemy2 and dist2: the name and the distance to enemy 2.

Before your turn is over (end of the loop), output the value of either enemy1 or enemy2 to shoot the closest enemy.
'''
import sys
import math

# CodinGame planet is being attacked by slimy insectoid aliens.
# <---
# Hint:To protect the planet, you can implement the pseudo-code provided in the statement, below the player.


# game loop
while True:
    enemy_1 = input()  # name of enemy 1
    dist_1 = int(input())  # distance to enemy 1
    enemy_2 = input()  # name of enemy 2
    dist_2 = int(input())  # distance to enemy 2

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # You have to output a correct ship name to shoot ("Buzz", enemy1, enemy2, ...)

    if dist_1 < dist_2:
        print(enemy_1)
    else:
        print(enemy_2)