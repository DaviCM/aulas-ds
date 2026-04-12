import React, { useState } from "react";
import { View, Text, Image, TouchableOpacity, StyleSheet } from "react-native";

async function getPokemonData(index) {}

export default function App() {
  const [index, setIndex] = useState(1);

  return (
    <View style={styles.fundo}>
      <View style={styles.containerLogo}>
        <Image
          style={styles.logo}
          source={require("./assets/pokemon-logo.png")}
        />
      </View>

      <View style={styles.containerImgPokemon}>
        <Image
          style={styles.imgPokemon}
          source={require("./assets/placeholder.svg")}
        />
      </View>

      <Text style={styles.textoNumeroPokemon}>#{index}</Text>

      <View style={styles.containerInfoPokemon}>
        <Text style={styles.textoInfoPokemon}>Species: Blastoise </Text>
        <Text style={styles.textoInfoPokemon}>Type 1: Water </Text>
        <Text style={styles.textoInfoPokemon}>Type 2: None </Text>
      </View>

      <View style={styles.containerBtn}>
        <TouchableOpacity style={styles.btn}>
          <Text
            style={styles.textoBtn}
            onPress={index > 1 ? () => setIndex((index) => index - 1) : null}
          >
            Anterior
          </Text>
        </TouchableOpacity>

        <TouchableOpacity style={styles.btn}>
          <Text
            style={styles.textoBtn}
            onPress={index < 1025 ? () => setIndex((index) => index + 1) : null}
          >
            Próximo
          </Text>
        </TouchableOpacity>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  fundo: {
    flex: 1,
    backgroundColor: "#d6d6d6",
  },

  containerLogo: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center", // referente ao eixo perpendicular ao flex
    marginTop: 10,
    marginHorizontal: 35,
    borderRadius: 15,
    backgroundColor: "#ca4141",
  },

  logo: {
    aspectRatio: 3840 / 1410,
    width: "70%",
    height: "auto",
  },

  containerImgPokemon: {
    flex: 2.5,
    flexDirection: "row",
    justifyContent: "center",
    alignItems: "center",
    marginTop: 10,
    marginHorizontal: 20,
    borderRadius: 15,
    backgroundColor: "#2c2c2c",
    borderWidth: 5,
    borderColor: "#ca4141",
  },

  imgPokemon: {
    aspectRatio: 326 / 413,
    width: "55%",
    height: "auto",
  },

  textoNumeroPokemon: {
    alignSelf: "center",
    fontFamily: "helvetica",
    fontSize: 30,
    fontWeight: "bold",
    margin: 15,
    color: "#2c2c2c",
  },

  containerInfoPokemon: {
    flex: 1.5,
    justifyContent: "center",
    alignItems: "flex-start",
    marginHorizontal: 20,
    marginBottom: 10,
    borderRadius: 15,
    backgroundColor: "#2c2c2c",
    borderWidth: 5,
    borderColor: "#ca4141",
  },

  textoInfoPokemon: {
    fontFamily: "helvetica",
    fontSize: 20,
    fontWeight: "bold",
    marginLeft: 20,
    marginVertical: 15,
    color: "#d6d6d6",
  },

  containerBtn: {
    flex: 1.5,
    flexDirection: "row",
    justifyContent: "center",
    alignItems: "flex-start",
    marginHorizontal: 20,
  },

  btn: {
    padding: 20,
    marginHorizontal: 10,
    borderRadius: 15,
    backgroundColor: "#ca4141",
    borderWidth: 4,
    borderColor: "#2c2c2c",
  },

  textoBtn: {
    fontFamily: "helvetica",
    fontSize: 25,
    fontWeight: "bold",
    color: "#d6d6d6",
  },
});
