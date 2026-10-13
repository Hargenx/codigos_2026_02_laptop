import { View, Text } from 'react-native';

export default function App() {

  function somar(a, b) {
    return a + b;
  }

  const resultado = somar(5, 3);

  return (
    <View>
      <Text>5 + 3 = {resultado}</Text>
    </View>
  );
}