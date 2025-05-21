//primitive data types   
//7 types : (call by value ) String, Number, Boolean, Null, Undefined, Symbol(unique), BigInt

//Non-primitive data types   -> refrence types (call by reference)
//3 types : Object, Array, Functions 
//Object => collection of key value pairs
//Array => collection of values
//Function => collection of code

//it is dynamic language and not static as variables can hold values of different types during runtime

const score = 100; //number
const scoreString = 100.3 //number
const isLoggedIn = true; //boolean
const outsideTemp = null; //null
const outsideTemp1 = undefined; //undefined
const bigInt = BigInt(1234567890123456789012345678901234567890); //bigint
const bignumber = 1234567890123456789012345678901234567890n; //bigint
const symbol = Symbol("I am a symbol"); //symbol
const symbol2 = Symbol("I am a symbol"); //symbol
console.log(typeof symbol); //symbol
console.log(typeof symbol2); //symbol
console.log(symbol === symbol2); //false


const obj = {name: "Ashant", age: 23}; //object
const arr = [1, 2, 3, 4, 5]; //array
const arr1 =["Ashant", 23, true, null, undefined]; //array
const func = function() { //function
    console.log("Hello World");
} //function
const func1 = () => { //arrow function
    console.log("Hello World");
} //arrow function

console.log(typeof score); //number
console.log(typeof scoreString); //number
console.log(typeof isLoggedIn); //boolean
console.log(typeof outsideTemp); //object
console.log(typeof outsideTemp1); //undefined
console.log(typeof bigInt); //bigint
console.log(typeof bignumber); //bigint
console.log(typeof obj); //object
console.log(typeof arr); //object
console.log(typeof func); //function
console.log(typeof func1); //function
console.log(typeof symbol); //symbol
console.log(typeof symbol2); //symbol
console.log(typeof arr1); //object
console.log(typeof null); //object
console.log(typeof undefined); //undefined
console.log(typeof Symbol("I am a symbol")); //symbol
//non primitive return type is object only function object function so returns as function
// https://262.ecma-international.org/5.1/#sec-11.4.3