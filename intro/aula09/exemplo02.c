#include <stdio.h>
int main(void) {
    float notas[4], soma = 0;
    for (int i = 0; i < 4; i++) {
        printf("Digite a nota %d: ", i + 1);
        scanf("%f", &notas[i]);
        soma += notas[i];
    }
    printf("A media das notas é: %.2f\n", soma / 4);
    return 0;
}