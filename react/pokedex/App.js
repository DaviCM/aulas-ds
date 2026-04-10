import React, { Component } from "react";
import { View, Text, Image, TouchableOpacity, StyleSheet } from "react-native";
import { StatusBar } from "expo-status-bar";

export default function App() {
  return (
    <View style={styles.fundo}>
      <View style={styles.areaCabecalho}>
        <Image
          style={styles.logo}
          source={require("./assets/pokemon-logo.png")}
        />
      </View>

      <View style={styles.areaImagem}>
        <Image
          style={styles.imgPokemon}
          source={require("./assets/pokemon-logo.png")}
        />

        <View style={styles.descPokemon}>
          <Text>Nome: </Text>
        </View>

        <View style={styles.descPokemon}>
          <Text>Tipo: </Text>
        </View>
      </View>

      <View style={styles.areaBotoes}></View>
    </View>
  );
}

const styles = StyleSheet.create({
  fundo: {
    flex: 1,
    justifyContent: "top",
    alignItems: "center",
  },

  areaCabecalho: {
    flex: 1,
    backgroundColor: "red",
  },

  logo: {
    width: 400,
    height: 140,
    marginTop: 20,
  },

  areaImagem: {
    flex: 3,
    gap: 6,
    backgroundColor: "green",
  },

  imgPokemon: {
    width: 400,
    height: 150,
  },

  descPokemon: {
    flex: 1,
    gap: 6,
    flexDirection: "row",
    color: "black",
    fontFamily: "consolas",
    fontSize: "10",
    fontWeight: "bold",
    backgroundColor: "blue",
  },
});
