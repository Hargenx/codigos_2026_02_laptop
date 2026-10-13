#include <stdio.h>

int main(void) {
    double renda, valor_solicitado;

    printf("Introduza a renda mensal: ");
    if (scanf("%lf", &renda) != 1) return 1;

    printf("Introduza o valor solicitado: ");
    if (scanf("%lf", &valor_solicitado) != 1) return 1;

    if (renda < 0 || valor_solicitado < 0) {
        puts("Valores invalidos. A renda e o valor solicitado devem ser positivos.");
        return 1;
    }

    if (renda < 2000.0) {
        puts("Analise manual");
    } else {
        if (valor_solicitado <= (0.30 * renda)) {
            puts("Credito aprovado.");
        } else {
            puts("Credito recusado.");
        }
    }

    return 0;
}