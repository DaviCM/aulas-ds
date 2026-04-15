import React, { useState, useEffect } from "react";
import { View, Text, Image, TouchableOpacity, StyleSheet } from "react-native";

async function pegarDadosPoke(index) {
  const data = await fetch(`https://pokeapi.co/api/v2/pokemon/${index}`);
  let types = [];

  if (data.status == 200) {
    const poke = await data.json();

    if (poke.types.length > 1) {
      types = [poke.types[0].type.name, poke.types[1].type.name];
    } else {
      types = [poke.types[0].type.name];
    }

    return {
      name: poke.name,
      types: types,
      sprite_url: poke.sprites.other.dream_world.front_default,
    };
  }
}

async function pegarSpriteTiposPoke(type) {
  const data = await fetch(`https://pokeapi.co/api/v2/type/${type}`);

  if (data.status == 200) {
    const typeInfo = await data.json();
    return typeInfo.sprites["generation-viii"]["sword-shield"].name_icon;
  }
}

export default function App() {
  const [index, setIndex] = useState(1);
  const [name, setName] = useState("");
  const [types, setTypes] = useState([]);
  const [sprite, setSprite] = useState("");
  const [spriteTypes, setSpriteTypes] = useState([]);

  useEffect(() => {
    pegarDadosPoke(index).then((info) => {
      setName(info.name);
      setTypes(info.types);
      setSprite(info.sprite_url);
    });

    async function alocarSprites() {
      const newSpriteTypes = await Promise.all(
        types.map((type) => pegarSpriteTiposPoke(type)),
      );

      setSpriteTypes(newSpriteTypes);
      console.log(newSpriteTypes);
    }

    alocarSprites();
  }, [index]);

  // lembrete: encadear funções faz o valor de cada uma delas ser retornado para a próxima, e iso pode causar diversos problemas.

  return (
    <View style={styles.fundo}>
      <View style={styles.containerLogo}>
        <Image
          style={styles.logo}
          source={require("./assets/pokemon-logo.png")}
        />
      </View>

      <View style={styles.containerImgPokemon}>
        <Image style={styles.imgPokemon} source={{ uri: sprite }} />
      </View>

      <Text style={styles.textoNumeroPokemon}>#{index}</Text>

      <View style={styles.containerInfoPokemon}>
        <Text style={styles.textoInfoPokemon}>Espécie: {name}</Text>
        <Image style={styles.spriteTipo} source={{ uri: spriteTypes[0] }} />
        <Image style={styles.spriteTipo} source={{ uri: spriteTypes[1] }} />
      </View>

      <View style={styles.containerBtn}>
        <TouchableOpacity
          style={styles.btn}
          onPress={index > 1 ? () => setIndex((index) => index - 1) : null}
        >
          <Text style={styles.textoBtn}>Anterior</Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={styles.btn}
          onPress={index < 1025 ? () => setIndex((index) => index + 1) : null}
        >
          <Text style={styles.textoBtn}>Próximo</Text>
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
    borderWidth: 4,
    borderColor: "#2c2c2c",
  },

  logo: {
    aspectRatio: 3840 / 1410,
    width: "70%",
    height: "auto",
    resizeMode: "contain",
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
    resizeMode: "contain",
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

  spriteTipo: {
    aspectRatio: 200 / 44,
    width: "40%",
    height: "auto",
    resizeMode: "contain",
    marginLeft: 20,
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
