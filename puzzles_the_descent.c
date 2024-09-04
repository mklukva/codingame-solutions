/*Your program must destroy the enemy ships by shooting the closest enemy on each turn.
Rules
On each start of turn (within the game loop), you obtain information on the two closest enemies:

-enemy1 and dist1: the name and the distance to enemy 1.
-enemy2 and dist2: the name and the distance to enemy 2.

Before your turn is over (end of the loop), output the value of either enemy1 or enemy2 to shoot the closest enemy.
*/


#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {

  // game loop
  while (1) {
    // name of enemy 1
    char enemy_1[257];
    scanf("%s", enemy_1);
    getchar(); 
    // distance to enemy 1
    int dist_1;
    scanf("%d", &dist_1);
    getchar(); 
    // name of enemy 2
    char enemy_2[257];
    scanf("%s", enemy_2);
    getchar(); 
    // distance to enemy 2
    int dist_2;
    scanf("%d", &dist_2);
    getchar(); 

    // Write an action using printf(). DON'T FORGET THE TRAILING 
    if (dist_1 < dist_2)
        printf("%s\n", &enemy_1); 
    else
        printf("%s\n", &enemy_2);
  }
  return 0;
}
