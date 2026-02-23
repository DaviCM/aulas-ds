// function getInt(message) {
//     while (true) {
//         try {
//             let num = (prompt(message).replace(',', '.')).trim()
//             return Number(num);
//         }
//         catch (error) {
//             console.log('Valor inválido. Tente novamente.')
//             continue
//         };
//     };
// };


function calc() {
    while (true) {
        // let num1 = getInt('Digite o primeiro número: ');
        // let num2 = getInt('Digite o segundo número: ');

        let num1 = Number(prompt('Digite o primeiro número: '));
        let num2 = Number(prompt('Digite o segundo número: '));

        console.clear();

        console.log('1 - Soma');
        console.log('2 - Subtração');
        console.log('3 - Multiplicação');
        console.log('4 - Divisão \n');
        choice = prompt('Digite a operação que deseja realizar:');

        switch (choice) {
            case '1':
                console.log(num1 + num2);
            case '2':
                console.log(num1 - num2);
            case '3':
                console.log(num1 * num2);
            case '4':
                console.log(num1 / num2);
            default: // muito melhor que o python, meu deus!
                console.clear();
                console.log('Valor inválido. Por favor, tente novamente.');

        };
    };
};

calc();