import { View, Text } from 'react-native';

export default function App() {

  const multiplicar = (x, y) => x * y;
  const dividir = (a, b) => a / b;

  return (
    <View>
      <Text>Multiplicação: {multiplicar(4, 3)}</Text>
      <Text>Divisão: {dividir(10, 2)}</Text>
    </View>
  );
}