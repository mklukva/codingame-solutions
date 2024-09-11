/*
Your program must read the data from the standard input and write the result on the standard output.
Input:
Line 1: N, the number of temperatures to analyze
Line 2: A string with the N temperatures expressed as integers ranging from -273 to 5526
Output:
Display 0 (zero) if no temperatures are provided. Otherwise, display the temperature closest to 0.
Constraints
0 ≤ N < 10000
*/
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int compare(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int func(int *pos, int pos_len, int *neg, int neg_len) {
    if (pos_len == 0 && neg_len == 0) {
        return 0; // Edge case if both are empty
    }
    if (neg_len > 0 && pos_len > 0) {
        return (pos[0] <= abs(neg[neg_len - 1])) ? pos[0] : neg[neg_len - 1];
    } else if (neg_len == 0 && pos_len > 0) {
        return pos[0];
    } else if (pos_len == 0 && neg_len > 0) {
        return neg[neg_len - 1];
    }
    return 0; // Default return
}

int main() {
    int n;
    scanf("%d", &n);
    
    int *lst = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        scanf("%d", &lst[i]);
    }

    qsort(lst, n, sizeof(int), compare);

    int *negative = (int *)malloc(n * sizeof(int));
    int *positive = (int *)malloc(n * sizeof(int));
    int neg_count = 0, pos_count = 0;

    for (int i = 0; i < n; i++) {
        if (lst[i] < 0) {
            negative[neg_count++] = lst[i];
        } else if (lst[i] > 0) {
            positive[pos_count++] = lst[i];
        }
    }

    int result = func(positive, pos_count, negative, neg_count);
    printf("%d\n", result);

    free(lst);
    free(negative);
    free(positive);
    
    return 0;
}