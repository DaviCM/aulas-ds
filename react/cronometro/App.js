import React, { Component } from "react";
import { View, Text, Image, TouchableOpacity, StyleSheet } from "react-native";

// Essa classe herda de component
class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      numero: 0.0,
      botao: "Iniciar",
    };

    this.timer = null;

    this.iniciar = this.iniciar.bind(this);
    this.resetar = this.resetar.bind(this);
  }

  iniciar() {
    if (this.timer != null) {
      clearInterval(this.timer);
      this.timer = null;

      this.setState({ botao: "Iniciar" });
    } else {
      this.timer = setInterval(() => {
        this.setState({ numero: this.state.numero + 0.01 });
      }, 10);

      this.setState({ botao: "Parar" });
    }
  }

  resetar() {
    clearInterval(this.timer);
    this.timer = null;
    this.setState({
      numero: 0.0,
      botao: "Iniciar",
    });
  }

  render() {
    return (
      <View style={styles.container}>
        <Image style={styles.img} source={require("./assets/cronometro.png")} />
        <Text style={styles.textoImg}>{this.state.numero.toFixed(2)}</Text>

        <View style={styles.btnArea}>
          <TouchableOpacity style={styles.btn} onPress={this.iniciar}>
            <Text style={styles.btnTexto}>{this.state.botao}</Text>
          </TouchableOpacity>

          <TouchableOpacity style={styles.btn} onPress={this.resetar}>
            <Text style={styles.btnTexto}>Resetar</Text>
          </TouchableOpacity>
        </View>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1, // Esse container ocupa todo o espaço da tela
    backgroundColor: "deepskyblue",
    alignItems: "center",
    justifyContent: "center",
  },

  img: {},

  textoImg: {
    fontFamily: "consolas",
    color: "aliceblue",
    fontSize: 60,
    fontWeight: "bold",
    marginTop: -150,
    marginBottom: 120,
  },

  btnArea: {
    flexDirection: "row",
    marginTop: 20,
    height: 60,
  },

  btn: {
    backgroundColor: "aliceblue",
    flex: 1,
    height: 50,
    margin: 12,
    padding: 20,
    borderRadius: 9,
    alignItems: "center",
    justifyContent: "center",
  },

  btnTexto: {
    fontSize: 20,
    fontWeight: "bold",
    color: "deepskyblue",
  },
});

// irá expor a nossa classe para todos os componentes
// Nesse caso, para ser excutada pelo index.js
export default App;
