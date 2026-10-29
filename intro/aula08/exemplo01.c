
#include <stdio.h>

int main(void) {
    float numero1;
    float numero2;
    char operacao;

    printf("Digite o primeiro numero: ");
    scanf("%f", &numero1);

    printf("Digite a operacao (+, -, *, /): ");
    scanf(" %c", &operacao);

    printf("Digite o segundo numero: ");
    scanf("%f", &numero2);

    switch (operacao) {
        case '+':
            printf("Resultado: %.2f\n", numero1 + numero2);

            if (numero1 + numero2 > 0) {
                printf("O resultado e positivo.\n");
            } else if (numero1 + numero2 < 0) {
                printf("O resultado e negativo.\n");
            } else {
                printf("O resultado e zero.\n");
            }
            break;

        case '-':
            printf("Resultado: %.2f\n", numero1 - numero2);

            if (numero1 > numero2) {
                printf("O primeiro numero e maior.\n");
            } else if (numero1 < numero2) {
                printf("O segundo numero e maior.\n");
            } else {
                printf("Os numeros sao iguais.\n");
            }
            break;

        case '*':
            printf("Resultado: %.2f\n", numero1 * numero2);

            if (numero1 == 0 || numero2 == 0) {
                printf("Multiplicacao por zero.\n");
            } else if (numero1 * numero2 > 0) {
                printf("O produto e positivo.\n");
            } else {
                printf("O produto e negativo.\n");
            }
            break;

        case '/':
            if (numero2 != 0) {
                printf("Resultado: %.2f\n", numero1 / numero2);

                if (numero1 == 0) {
                    printf("O resultado e zero.\n");
                } else if (numero1 / numero2 >= 1) {
                    printf("O resultado e maior ou igual a 1.\n");
                } else {
                    printf("O resultado e menor que 1.\n");
                }
            } else {
                printf("Nao e possivel dividir por zero.\n");
            }
            break;

        default:
            printf("Operacao invalida!\n");
            break;
    }

    return 0;
}
