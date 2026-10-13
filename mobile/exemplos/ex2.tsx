import { View, Text } from 'react-native';

interface Pessoa {
  nome: string;
  idade: number;
}

export default function App() {

  const aluno: Pessoa = {
    nome: "Raphael",
    idade: 42
  };

  return (
    <View>
      <Text>Nome: {aluno.nome}</Text>
      <Text>Idade: {aluno.idade}</Text>
    </View>
  );
}