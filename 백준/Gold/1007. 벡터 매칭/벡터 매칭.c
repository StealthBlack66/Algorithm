#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <float.h>

typedef struct {
    int x;
    int y;
} Point;

double vector_length(double x, double y) {
    return sqrt(x * x + y * y);
}

double min_vector_matching(Point* points, int n) {
    int half_n = n / 2;
    int comb_size = 1 << n;
    double min_length = DBL_MAX;
    
    for (int i = 0; i < comb_size; ++i) {
        if (__builtin_popcount(i) == half_n) {
            double sum_x = 0;
            double sum_y = 0;

            for (int j = 0; j < n; ++j) {
                if (i & (1 << j)) {
                    sum_x += points[j].x;
                    sum_y += points[j].y;
                } else {
                    sum_x -= points[j].x;
                    sum_y -= points[j].y;
                }
            }

            double length = vector_length(sum_x, sum_y);
            if (length < min_length) {
                min_length = length;
            }
        }
    }

    return min_length;
}

int main() {
    int T;
    scanf("%d", &T);

    while (T--) {
        int N;
        scanf("%d", &N);
        Point* points = (Point*)malloc(N * sizeof(Point));

        for (int i = 0; i < N; ++i) {
            scanf("%d %d", &points[i].x, &points[i].y);
        }

        double result = min_vector_matching(points, N);
        printf("%.12f\n", result);

        free(points);
    }

    return 0;
}