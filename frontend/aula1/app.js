console.log('Olá, mundo!');

// comentário de linha, finalmente da forma certa!

/* 
comentários 
de 
bloco!
*/

// variáveis
var nome = 'Davi'; // global
let resposta = 42; // variável de escopo ou bloco
const pi = 3.14; // constante

console.log(nome, resposta, pi);

let num1 = 10
let num2 = 30

// operadores matemáticos
let sum = num1 + num2;
let sub = num1 - num2;
let mult = num1 * num2;
let div = num1 / num2;
let rest = num1 % num2;

// operadores lógicos
let bigger = num1 > num2;
let smaller = num1 < num2;
let equal = num1 == num2;
let strictly_equal = num1 === num2;

// para desigualdade, será !=.
// para desigualdade estrita (valor e tipo), !==

// operador AND
console.log(num1 && num2);

// operador OR
console.log(num1 || num2);

// operador NOT
console.log(!num2);

// concatenação de strings: , com espaço e + sem.
console.log('nome: ' + nome, 'resposta: ' + resposta);

// interpolação de acento grave: f-sting do js
console.log(`nome: ${nome}, resposta: ${resposta}`);

// operador ternario
let idade = 18
resultado = (idade >= 18) ? 'Maior de idade' : 'Menor de idade'; // super easy!
console.log(resultado);

// for loop!
for (let i = 0; i <= 6; i++) {
    console.log(i);
};

// manipulação de lista
let frutas = ['maçã', 'laranja', 'uva', 'banana'];
console.log(frutas[0]);
console.log(frutas.length);

// JSON
let maho = {
    nome : 'Maho',
    idade : 18,
    escola : 'Kuromorimine'
};

let lula = {
    nome: 'Lula',
    idade: 80,
    peso: 87,
    altura: 1.68
};

let imc_lula = lula.peso / (lula.altura * lula.altura);
console.log(`O Índice de Massa Corporal do Presidente Lula é: ${imc_lula}`);
if (imc_lula < 20) {
    console.log('Lula está magro.');
}
else if (imc_lula < 25) {
    console.log('O peso do presidente está normal.')
}
else if (imc_lula < 30) {
    console.log('Lula está levemente acima do peso.')
}
else if (imc_lula < 35) {
    console.log('Lula está bastante acima do peso. Hora de fazer uma caminhada!')
}
else {
    console.log('Definitivamente, o presidente não está bem.')
}

// for loop a partir de lista e de objeto (JSON)
let comandantes = ['Maho', 'Darjeeling', 'Kay', 'Katyusha', 'Alice', 'Marie'];
for (comandante of comandantes) {
    console.log(comandante);
};

let tanques = {
    'Panzer IV': 'Ausf. F2',
    'Tiger': 'Ausf. E',
    'Churchill': 'Mk. VII',
    'Sherman': 'M4A1',
    'Centurion': 'Mk. I',
    'Carro Veloce': 'CV33'
}

for (let tanque in tanques) {
    console.log('Tanque: ' + tanque, 'Especificação: ' + tanques[tanque])
}

// toFixed: função que arredonda o valor para um número fixo de casas decimais
// como :xf no Python.
console.log(`${num1.toFixed(2)}`)