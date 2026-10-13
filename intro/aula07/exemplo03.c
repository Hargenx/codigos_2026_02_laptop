#include <stdio.h>

int main(void) {
    int opcao;
    puts("=== MENU ===");
    puts("1 - Consultar saldo");
    puts("2 - Solicitar suporte");
    puts("3 - Encerrar");
    printf("Escolha: ");
    if (scanf("%d", &opcao) != 1) {
        puts("Entrada invalida.");
        return 1;
    }
    switch (opcao) {
        case 1: puts("Saldo disponivel."); break;
        case 2: puts("Abrindo chamado."); break;
        case 3: puts("Ate logo!"); break;
        default: puts("Opcao inexistente.");
    }
    return 0;
}