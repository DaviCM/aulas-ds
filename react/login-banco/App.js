import React, { Component } from "react";
import {
  View,
  Text,
  TextInput,
  Switch,
  TouchableOpacity,
  StyleSheet,
} from "react-native";
import { Picker } from "@react-native-picker/picker";
import Slider from "@react-native-community/slider";

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      nome: "",
      idade: 0,
      genero: "",
      limite: 0.0,
      isEstudante: false,
    };

    this.novoNome;
    this.novaIdade;
    this.novoGenero;
    this.novoLimite;

    this.atualizarNome = this.atualizarNome.bind(this);
    this.atualizarIdade = this.atualizarIdade.bind(this);
    this.atualizarGenero = this.atualizarGenero.bind(this);
    this.atualizarLimite = this.atualizarLimite.bind(this);
    this.toggleEstudante = this.toggleEstudante.bind(this);
  }

  atualizarNome() {
    this.setState({ nome: this.novoNome });
  }

  atualizarIdade() {
    this.setState({ idade: this.novaIdade });
  }

  atualizarGenero() {
    this.setState({ genero: this.novoGenero });
  }

  atualizarLimite() {
    this.setState({ limite: this.novoLimite });
  }

  toggleEstudante() {
    this.setState({ isEstudante: !isEstudante });
  }

  render() {
    return (
      <View style={styles.fundo}>
        <View style={styles.caixaDeOpcoes}>
          <TextInput
            style={styles.input}
            inputMode="text"
            value={this.novoNome}
            onChangeText={this.atualizarNome}
            autoCapitalize="words"
            placeholder="Insira seu nome: "
          />

          <TextInput
            style={styles.input}
            inputMode="numeric"
            maxLength={3}
            value={this.novaIdade}
            onChangeText={this.atualizarIdade}
            placeholder="Insira sua idade: "
          />

          <Picker
            style={styles.picker}
            mode="dropdown"
            selectedValue={this.novoGenero}
            onValueChange={this.atualizarGenero}
          >
            <Picker.Item label="Masculino" value="Masculino" />
            <Picker.Item label="Feminino" value="Feminino" />
          </Picker>

          <Slider
            style={styles.slider}
            minimumValue={500}
            maximumValue={45000}
            step={500}
            value={this.novoLimite}
            onValueChange={this.atualizarLimite}
          />
          <Text style={styles.textoSlider}>{this.novoLimite}</Text>
        </View>

        <View style={styles.caixaSwitch}>
          <Switch
            style={styles.switch}
            trackColor={{ false: "dimgrey", true: "deepskyblue" }}
            thumbColor={this.state.isEstudante ? "aliceblue" : "lightgrey"}
            onValueChange={this.toggleEstudante}
          />
          <Text style={styles.textoSwitch}>Conta para Estudante</Text>
        </View>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  fundo: {
    flex: 1,
    backgroundColor: "mintcream",
    alignContent: "center",
    justifyContent: "center",
  },

  caixaDeOpcoes: {
    backgroundColor: "lightblue",
    flexDirection: "column",
    padding: 10,
    margin: 30,
    marginTop: 10,
    marginBottom: 10,
    borderRadius: 10,
    alignContent: "center",
    justifyContent: "center",
  },

  input: {
    backgroundColor: "aliceblue",
    borderStyle: "solid",
    borderWidth: 2,
    borderColor: "lightseagreen",
    fontFamily: "consolas",
    fontWeight: "bold",
    fontSize: 15,
    color: "lightseagreen",
    padding: 10,
    marginHorizontal: 20,
    marginVertical: 10,
    borderRadius: 10,
  },

  picker: {
    backgroundColor: "aliceblue",
    borderStyle: "solid",
    borderWidth: 2,
    borderColor: "lightseagreen",
    fontFamily: "consolas",
    fontWeight: "bold",
    fontSize: 15,
    color: "lightseagreen",
    padding: 10,
    marginHorizontal: 20,
    marginVertical: 10,
    borderRadius: 10,
  },

  slider: {
    marginHorizontal: 20,
    marginTop: 30,
    marginBottom: 10,
  },

  textoSlider: {
    fontFamily: "consolas",
    fontWeight: "bold",
    fontSize: 15,
    color: "aliceblue",
    textAlign: "left",
  },

  caixaSwitch: {
    backgroundColor: "lightblue",
    flexDirection: "row",
    padding: 10,
    margin: 30,
    marginTop: 10,
    marginBottom: 10,
    borderRadius: 10,
    alignContent: "center",
    justifyContent: "center",
  },

  switch: {
    height: 20,
    marginRight: 30,
  },

  textoSwitch: {
    flex: 1,
    marginLeft: 30,
    fontFamily: "consolas",
    fontWeight: "bold",
    fontSize: 16,
    color: "lightseagreen",
    textAlign: "left",
  },
});

export default App;
