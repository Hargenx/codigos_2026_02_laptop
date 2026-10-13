import { View, Text } from 'react-native';

export default function App() {

  const alunos = [
    "Raphael",
    "Vinicius",
    "Gilson",
    "Sara"
  ];

  return (
    <View>
      <Text>Alunos:</Text>

      {alunos.map((aluno, indice) => (
        <Text key={indice}>
          {indice + 1} - {aluno}
        </Text>
      ))}
    </View>
  );
}