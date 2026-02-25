function a_pagar(usuario, tempo_gasto, vip) {
    let valor_a_pagar

    if (tempo_gasto >= 3) {
        valor_a_pagar = 20 + (8 * (tempo_gasto - 3));
    }
    else {
        valor_a_pagar = 8 * tempo_gasto;
    };

    // toFixed: método do tipo number do js, que arredonda ele para um número fixo de casas decimais
    if (vip == true) {
        console.log(`Nome: ${usuario}`);
        console.log(`Valor a pagar: R$ ${(valor_a_pagar * 0.8).toFixed(2)}`);
    }
    else {
        console.log(`Nome: ${usuario}`);
        console.log(`Valor a pagar: R$ ${valor_a_pagar.toFixed(2)}`);
    };

};

a_pagar('Nunes', 9, true);

