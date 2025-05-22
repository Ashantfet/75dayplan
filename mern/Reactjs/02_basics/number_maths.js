const score =100;

const balance = new Number(190); //object
console.log(balance); //Number { 190 }
console.log(score); //100

console.log(balance.toString().length); //190
console.log(typeof balance); //object

console.log((balance.toFixed(2))); //190.00
console.log(balance.toPrecision(2)); //1.9e+2

const num1 =123.8933
console.log((num1.toPrecision(2))); //1.2e+2

const hundreds = 1000000
console.log(hundreds.toLocaleString('en-IN')); //1,000,000

//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

//Math Object
console.log(Math) //Math { [Symbol: Math]: [Circular], E: 2.718281828459045, LN2: 0.6931471805599453, LN10: 2.302585092994046, LOG2E: 1.4426950408889634, LOG10E: 0.4342944819032518, PI: 3.141592653589793, SQRT1_2: 0.7071067811865476, SQRT2: 1.4142135623730951 }
console.log((Math.abs(-100))); //100
console.log(Math.round(100.4)); //100
console.log(Math.round(100.5)); //101
console.log(Math.floor(100.5)); //100
console.log(Math.ceil(100.5)); //101
console.log(Math.floor(-100.5)); //-101
console.log(Math.ceil(-100.5)); //-100

console.log(Math.max(100, 200, 300)); //300
console.log(Math.min(100, 200, 300)); //100
console.log(Math.random()); //anything between 0 and 1
console.log(Math.floor(Math.random() * 10)+ 1); //anything between 0 and 10
//floor make it a complete number

const min =10
const max =20

console.log((Math.random() * (max - min + 1)) + min)//anything between 10 and 20
console.log(Math.floor(Math.random() * (max - min + 1)) + min)//anything between 10 and 20