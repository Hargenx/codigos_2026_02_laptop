#include <stdio.h>

int main(void) {
    int matriculado, horarioPermitido;
    printf("Matriculado? (1/0): ");
    if (scanf("%d", &matriculado) != 1) return 1;
    printf("Horario permitido? (1/0): ");
    if (scanf("%d", &horarioPermitido) != 1) return 1;
    
    if (matriculado == 1) {
        if (horarioPermitido == 1) {
            puts("Entrada liberada.");
        } else {
            puts("Fora do horario.");
        }
    } else {
        puts("Matricula nao encontrada.");
    }
    return 0;
}