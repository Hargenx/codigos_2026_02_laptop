#include <stdio.h>
int main() {
    float nota1, nota2, media;
    printf("Digite a primeira nota: ");
    scanf("%f", &nota1);
    printf("Digite a segunda nota: ");
    scanf("%f", &nota2);
    media = (nota1 + nota2) / 2;
    printf("A media e: %.2f\n", media);
    printf("O aluno esta %s com a media %.1f %s\n", (media >= 6.0) ? "Aprovado" : "Reprovado", media, (int)nota2);
    return 0;
}