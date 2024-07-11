#include <stdio.h>

int get_last_digit(int a, int b) {
    if (b == 0) {
        return 1;
    }

    int cycle[4];
    cycle[0] = a % 10;
    for (int i = 1; i < 4; i++) {
        cycle[i] = (cycle[i - 1] * cycle[0]) % 10;
    }

    int cycle_length = 4;
    for (int i = 1; i < 4; i++) {
        if (cycle[i] == cycle[0]) {
            cycle_length = i;
            break;
        }
    }

    int index = (b - 1) % cycle_length;
    return cycle[index];
}

int main() {
    int T;
    scanf("%d", &T);

    for (int i = 0; i < T; i++) {
        int a, b;
        scanf("%d %d", &a, &b);

        int last_digit = get_last_digit(a, b);
        printf("%d\n", last_digit == 0 ? 10 : last_digit);
    }

    return 0;
}