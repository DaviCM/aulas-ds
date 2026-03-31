import React, { Component } from "react";
import {
  View,
  Text,
  Image,
  TouchableOpacity,
  FlatList,
  ScrollView,
  Dimensions,
  useWindowDimensions,
  StyleSheet,
} from "react-native";

// Essa classe herda de component
class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      numero: 0.0,
      botao: "Iniciar",
      alturaInicial: Dimensions.get("window").height,
    };

    this.temposSalvos = [];
    this.timer = null;

    this.iniciar = this.iniciar.bind(this);
    this.resetar = this.resetar.bind(this);
    //    this.iniciarScrollView = this.iniciarScrollView.bind(this);
    this.mostrarTemposSalvos = this.mostrarTemposSalvos.bind(this); // cria uma função que sempre terá 'this' como atributo, garantindo que ela mantenha contexto.
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

    if (this.state.numero > 0) {
      this.temposSalvos.push(this.state.numero);
    }

    this.setState({
      numero: 0.0,
      botao: "Iniciar",
    });
  }

  /*
  iniciarScrollView() {
    if (this.state.alturaInicial != useWindowDimensions().height) {
      return this.temposSalvos.length > 5;
    }
  }
*/

  mostrarTemposSalvos() {
    return (
      <View style={styles.historico}>
        <Text style={styles.tituloHistorico}>Histórico</Text>
        <FlatList
          data={this.temposSalvos}
          renderItem={({ item, index }) => {
            return (
              <View>
                <Text style={styles.tempoSalvo}>
                  {index + 1}. {item.toFixed(2)}
                </Text>
              </View>
            );
          }}
          inverted={true}
        />
      </View>
    );
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

        <ScrollView>
          <View>{this.mostrarTemposSalvos()}</View>
        </ScrollView>
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

  img: {
    marginTop: 180,
  },

  textoImg: {
    color: "aliceblue",
    fontSize: 60,
    fontFamily: "consolas",
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
    marginTop: -30,
    marginHorizontal: 12,
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

  scroll: {
    flex: 1,
    showsVerticalScrollIndicator: "true",
  },

  historico: {
    backgroundColor: "aliceblue",
    flex: 1,
    padding: 15,
    marginTop: 0,
    borderRadius: 9,
    alignItems: "center",
    justifyContent: "center",
  },

  tituloHistorico: {
    color: "deepskyblue",
    fontSize: 25,
    fontFamily: "consolas",
    fontWeight: "bold",
    marginBottom: 15,
  },

  tempoSalvo: {
    color: "deepskyblue",
    fontSize: 25,
    fontFamily: "consolas",
    padding: 10,
  },
});

// irá expor a nossa classe para todos os componentes
// Nesse caso, para ser excutada pelo index.js
export default App;
