"use strict";  //treat all JS code as newer version

//alert("Hello World"); //we are using nodejs  //alert box
//alert("3+2  "); //alert box
//code readability should be kept in mind 
console.log("Hello World"); //console box
console.log(3+2); //console box
console.log("3+2  "); //console box

let name = "Ashant"; //string
let age = 23; //number
let isLoggedIn = true; //boolean
//number =>2^53
//bigint => 2^53
let bigInt = BigInt(1234567890123456789012345678901234567890); //bigint
//boolean => true/false
//null => empty value standalone value 
//undefined => value not assigned value not assigned
//symbol => unique value and not accessible
//object => collection of key value pairs
console.log(typeof "Ashant"); //string
console.log(typeof 23); //number
console.log(typeof true); //boolean
console.log(typeof null); //object
console.log(typeof undefined); //undefined
console.log(typeof bigInt); //bigint
console.log(typeof Symbol("I am a symbol")); //symbol
console.log(typeof {name: "Ashant", age: 23}); //object