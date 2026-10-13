#include <stdio.h>

int main() {
    char nome[7] = "Raphael";
    int idade = 42;
    float altura = 1.83;
    double salario = 19000.50;
    printf("Nome: %s\n", nome);
    printf("Idade: %d\n", idade);
    printf("Altura: %.2f\n", altura);
    printf("Salário: %.2f\n", salario);
    printf("Tamanho do nome: %lu\n", sizeof(nome));
    printf("Tamanho do tipo int: %lu\n", sizeof(int));
    printf("Tamanho do tipo float: %lu\n", sizeof(float));
    printf("Tamanho do tipo double: %lu\n", sizeof(double));
    return 0;
}