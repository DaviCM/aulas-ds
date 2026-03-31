import React, { Component } from "react";
import {
  View,
  Text,
  TextInput,
  Switch,
  TouchableOpacity,
  Modal,
  StyleSheet,
} from "react-native";
import { Picker } from "@react-native-picker/picker";
import Slider from "@react-native-community/slider";

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      nome: "",
      idade: "",
      genero: "",
      limite: "",
      isEstudante: false,
      modal: false,
    };

    this.modalCriarConta = this.modalCriarConta.bind(this);
  }

  modalCriarConta() {
    if (
      this.state.nome == "" ||
      this.state.idade == "" ||
      this.state.genero == "" ||
      this.state.limite == ""
    ) {
      return (
        <Modal
          style={styles.modalCriarConta}
          animationType="fade"
          transparent="true"
          visible={this.state.modal}
          onRequestClose={(modal) => this.setState({ modal })}
        >
          <Text>Há informações que ainda não foram preenchidas,</Text>
          <Text>Preencha todas para prosseguir.</Text>
        </Modal>
      );
    }
  }

  render() {
    return (
      <View style={styles.fundo}>
        <View style={styles.caixaDeOpcoes}>
          <TextInput
            style={styles.input}
            inputMode="text"
            value={this.state.nome}
            onChangeText={(nome) => this.setState({ nome })}
            autoCapitalize="words"
            placeholder="Insira seu nome: "
          />

          <TextInput
            style={styles.input}
            inputMode="numeric"
            maxLength={3}
            value={this.state.idade}
            onChangeText={(idade) => this.setState({ idade })}
            placeholder="Insira sua idade: "
          />

          <Picker
            style={styles.picker}
            mode="dropdown"
            selectedValue={this.state.genero}
            onValueChange={(genero) => this.setState({ genero })}
            prompt="Escolha seu gênero: "
          >
            <Picker.Item label="Escolha seu gênero: " value={""} />
            <Picker.Item label="Masculino" value="Masculino" />
            <Picker.Item label="Feminino" value="Feminino" />
            <Picker.Item label="Outro" value="Outro" />
          </Picker>

          <Slider
            style={styles.slider}
            minimumTrackTintColor="lightseagreen"
            maximumTrackTintColor="darkgrey"
            thumbTintColor="seagreen"
            minimumValue={500}
            maximumValue={45000}
            step={500}
            value={this.state.limite}
            onValueChange={(limite) => this.setState({ limite })}
          />
          <Text style={styles.textoSlider}>
            Escolha seu limite: R${this.state.limite},00
          </Text>
        </View>

        <View style={styles.caixaSwitch}>
          <Switch
            style={styles.switch}
            trackColor={{ false: "dimgrey", true: "darkseagreen" }}
            thumbColor={this.state.isEstudante ? "seagreen" : "lightgrey"}
            activeThumbColor="seagreen"
            value={this.state.isEstudante}
            onValueChange={(isEstudante) => this.setState({ isEstudante })}
          />
          <Text style={styles.textoSwitch}>Conta para Estudante</Text>
        </View>

        <TouchableOpacity
          style={styles.botaoCriarConta}
          onPress={this.modalCriarConta}
        >
          <Text style={styles.textoBotao}>Criar Conta</Text>
        </TouchableOpacity>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  fundo: {
    flex: 1,
    backgroundColor: "aliceblue",
    alignContent: "center",
    justifyContent: "center",
  },

  caixaDeOpcoes: {
    backgroundColor: "lightblue",
    borderStyle: "solid",
    borderWidth: 2,
    borderColor: "lightseagreen",
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
    fontSize: 16,
    color: "lightseagreen",
    marginHorizontal: 20,
    textAlign: "left",
  },

  caixaSwitch: {
    backgroundColor: "lightblue",
    borderStyle: "solid",
    borderWidth: 2,
    borderColor: "lightseagreen",
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
    marginLeft: 20,
  },

  textoSwitch: {
    flex: 1,
    marginLeft: 15,
    fontFamily: "consolas",
    fontWeight: "bold",
    fontSize: 16,
    color: "lightseagreen",
    textAlign: "left",
  },

  modalCriarConta: {},

  botaoCriarConta: {
    backgroundColor: "lightblue",
    borderStyle: "solid",
    borderWidth: 2,
    borderColor: "lightseagreen",
    padding: 15,
    marginHorizontal: 350,
    marginVertical: 20,
    borderRadius: 10,
    alignContent: "center",
    justifyContent: "center",
  },

  textoBotao: {
    fontFamily: "consolas",
    fontWeight: "bold",
    fontSize: 18,
    color: "lightseagreen",
    textAlign: "center",
  },
});

export default App;
