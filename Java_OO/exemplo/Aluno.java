@Deprecated
@SuppressWarnings("deprecation")
public abstract strictfp class Aluno extends Pai implements Idealizacao, Sonho {
    //Atributo
    private String Nome;

    //Métodos (parcialmente mostrados)
    public void inserirNome() {
        Nome = System.in.toString();
    }

    public String recuperarNome() {
        return Nome;
        //... outros métodos ocultados por simplicidade
    }
}