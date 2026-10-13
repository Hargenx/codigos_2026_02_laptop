import { View, Text } from 'react-native';

export default function App() {

  const mensagem: string = "Olá, TypeScript!";
  const numero: number = 10;

  return (
    <View>
      <Text>{mensagem}</Text>
      <Text>{numero}</Text>
    </View>
  );
}