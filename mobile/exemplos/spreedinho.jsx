import { View, Text } from 'react-native';

export default function App() {

  const frutas = ["Maçã", "Banana"];
  const novasFrutas = [...frutas, "Morango", "Uva"];

  return (
    <View>
      {novasFrutas.map((fruta, indice) => (
        <Text key={indice}>
          {fruta}
        </Text>
      ))}
    </View>
  );
}