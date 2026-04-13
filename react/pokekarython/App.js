import { StatusBar } from "expo-status-bar";
import { StyleSheet, Text, View, Image, TouchableOpacity } from "react-native";
import React, { useState, useEffect } from "react";

export default function App() {
  const [id, setId] = useState(1);
  const [nome, setNome] = useState("");
  const [tipos, setTipos] = useState("");
  const [sprite, setSprite] = useState([""]);

  async function buscarPokemon(id) {
    const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${id}`);
    const poke = await response.json();
    let tiposPokemon = [];

    if (poke.types.length > 1) {
      tiposPokemon = [poke.types[0].type.name, poke.types[1].type.name];
    } else {
      tiposPokemon = [poke.types[0].type.name];
    }

    return {
      nome: poke.name,
      tipos: tiposPokemon,
      sprite: poke.sprites.front_default, // prettier-ignore
    };
  }

  useEffect(() => {
    // then manipula o resultado apenas depois que a Promise vira a resposta real
    buscarPokemon(id).then((info) => {
      setNome(info.nome);
      setTipos(info.tipos);
      setSprite(info.sprite);
    });
  }, [id]);

  return (
    <View style={styles.container}>
      <View style={styles.areaCabecalho}>
        <Image
          style={{ width: 400, height: 150 }}
          source={require("./assets/logo.png")}
        />
      </View>

      <View style={styles.areaImagem}>
        <View>
          <Image style={styles.imgPokemon} source={{ uri: sprite }} />
        </View>

        <View style={styles.descPokemon}>
          <Text>Nome:</Text>
          <Text>{nome}</Text>
        </View>

        <View style={styles.descPokemon}>
          <Text>Tipo 1:</Text>
          <Text>{tipos[0]}</Text>
          <Text>Tipo 2:</Text>
          <Text>{tipos[1]}</Text>
        </View>
      </View>

      <View style={styles.areaBotoes}>
        <TouchableOpacity style={styles.btn}>
          <Text
            style={styles.textBtn}
            onPress={id > 1 ? () => setId(id - 1) : null}
          >
            Previous
          </Text>
        </TouchableOpacity>

        <TouchableOpacity style={styles.btn}>
          <Text
            style={styles.textBtn}
            onPress={id < 1025 ? () => setId(id + 1) : null}
          >
            Next
          </Text>
        </TouchableOpacity>
      </View>

      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
  },

  areaCabecalho: {
    flex: 1,
    padding: 15,
  },

  areaImagem: {
    flex: 1,
    gap: 6,
    backgroundColor: "#23b802",
  },

  areaBotoes: {
    flex: 1,
    flexDirection: "row",
  },

  descPokemon: {
    flex: 1,
    flexDirection: "row",
    backgroundColor: "#9a2323",
    gap: 6,
    color: "#fff",
    padding: 10,
    justifyContent: "flex-start",
    alignItems: "center",
  },

  imgPokemon: {
    flex: 3,
    justifyContent: "center",
    alignItems: "center",
    padding: 15,
    width: 200,
    height: 200,
  },

  textBtn: {
    color: "#f8f8f8",
    fontSize: 16,
    fontWeight: "bold",
    alignItems: "center",
    justifyContent: "center",
  },

  btn: {
    flexDirection: "row",
    height: 30,
    borderRadius: 6,
    alignItems: "center",
    justifyContent: "center",
    padding: 10,
    margin: 15,
    backgroundColor: "rgb(28, 138, 234)",
  },
});
