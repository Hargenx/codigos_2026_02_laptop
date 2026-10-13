import { View, Text } from 'react-native';

interface PessoaProps {
  nome: string;
  idade: number;
}

function Pessoa({ nome, idade }: PessoaProps) {
  return (
    <View>
      <Text>{nome}</Text>
      <Text>{idade} anos</Text>
    </View>
  );
}

export default function App() {
  return (
    <Pessoa
      nome="Raphael"
      idade={40}
    />
  );
}