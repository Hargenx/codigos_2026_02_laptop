#include <stdio.h>

int main(void) {
    double media;
    printf("Informe a media (0 a 10): ");
    if (scanf("%lf", &media) != 1) {
        puts("Entrada invalida.");
        return 1;
    }
    if (media < 0 || media > 10) {
        puts("Media fora do intervalo.");
    } else if (media >= 7) {
        puts("Aprovado.");
    } else if (media >= 5) {
        puts("Recuperacao.");
    } else {
        puts("Reprovado.");
    }
    return 0;
}