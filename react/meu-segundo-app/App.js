import React, { Component } from 'react';
import { View, Text, Button, StyleSheet, TouchableOpacity } from 'react-native';

class App extends Component { // classe App herda de Component
  constructor(props) { // Props = propriedades
    super(props);

    this.state = {
      numero: 0,
    };

    this.alterarNumero = this.alterarNumero.bind(this);
  };


  alterarNumero(modo) {
    if (modo === 'soma') {
      this.setState({numero: this.state.numero + 1});
    }

    else if (modo === 'subtracao') {
      this.setState({numero: this.state.numero - 1});
    };
  };


  render() {
    return (
      <View style={styles.container}>
        <Text style={styles.titulo}>Meu Contador</Text><br/>

        <View style={styles.linhaBotoes}>

          <TouchableOpacity style={styles.botao} onPress={() => this.alterarNumero('soma')}>
            <Text style={styles.textoBotao}>Incrementar</Text>
          </TouchableOpacity>

          <Text style={styles.corpo}>{this.state.numero}</Text>
          
          <TouchableOpacity style={styles.botao} onPress={() => this.alterarNumero('subtracao')}>
            <Text style={styles.textoBotao}>Diminuir</Text>
          </TouchableOpacity>

        </View>
      </View>
    );
  };
};


const styles = StyleSheet.create ({
  container: {
    flex: 1,
    backgroundColor: '#242138',
    justifyContent: 'center',
    alignItems: 'center',
  },

  titulo: {
    color: 'deepskyblue',
    fontFamily: 'comic sans ms',
    fontSize: 50,
    fontWeight: 'bold',
  },

  corpo: {
    color: 'floralwhite',
    fontFamily: 'comic sans ms',
    fontSize: 40,
  },

  linhaBotoes: {
    flexDirection: 'row',
    gap: 20,
    width: '60%',
    justifyContent: 'center',
    alignContent: 'center',
  },

  botao: {
    backgroundColor: 'deepskyblue',
    borderRadius: 15,
    padding: 12,
  },

  textoBotao: {
    color: '#242138',
    fontFamily: 'comic sans ms',
    fontSize: 20,
    justifyContent: 'center',
    alignContent: 'center',
  }
});


export default App;

