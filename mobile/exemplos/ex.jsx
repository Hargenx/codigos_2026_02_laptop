import { View, Text } from 'react-native';

export default function App() {
  const mensagem = "Olá, JavaScript!";
  const numero = 10;

  return (
    <View>
      <Text>{mensagem}</Text>
      <Text>Número: {numero}</Text>
    </View>
  );
}