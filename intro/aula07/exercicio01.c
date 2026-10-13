#include <stdio.h>

int main(void) {
    int regiao;
    double valor_compra, frete, valor_total;

    printf("Introduza o codigo da regiao (1, 2 ou 3): ");
    if (scanf("%d", &regiao) != 1) {
        puts("Entrada invalida.");
        return 1;
    }

    switch (regiao) {
        case 1: 
            frete = 10.0; 
            break;
        case 2: 
            frete = 20.0; 
            break;
        case 3: 
            frete = 30.0; 
            break;
        default:
            puts("Regiao inexistente.");
            return 1;
    }

    printf("Introduza o valor da compra: R$ ");
    if (scanf("%lf", &valor_compra) != 1) {
        puts("Entrada invalida.");
        return 1;
    }

    if (valor_compra < 0) {
        puts("Valor invalido. A compra nao pode ser negativa.");
        return 1;
    }

    if (valor_compra >= 200.0) {
        frete = 0.0;
        puts("Frete gratis aplicado!");
    }

    valor_total = valor_compra + frete;
    
    printf("Valor do frete: R$ %.2f\n", frete);
    printf("Valor total a pagar: R$ %.2f\n", valor_total);

    return 0;
}