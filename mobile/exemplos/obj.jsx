import { View, Text } from 'react-native';

export default function App() {

  const pessoa = {
    nome: 'Raphael',
    idade: 42,
    cidade: 'Rio de Janeiro'
  };

  return (
    <View>
      <Text>Nome: {pessoa.nome}</Text>
      <Text>Idade: {pessoa.idade}</Text>
      <Text>Cidade: {pessoa.cidade}</Text>
    </View>
  );
}