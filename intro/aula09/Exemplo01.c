#include <stdio.h>
int main(void) {
    int idades[4] = {18, 19, 20, 21};
    float notas[3] = {7.5f, 8.0f, 9.5f};
    char letras[3] = {'A', 'B', 'C'};
    printf("%d\n", idades[0]);
    printf("%.1f\n", notas[1]);
    printf("%c\n", letras[2]);
    return 0;
}