 //let score = null it gives value in number as 0
let score = "100abc"; //string
 console.log((typeof score));
 console.log(typeof (score));
 
let valueinnumber = Number(score);
console.log(typeof valueinnumber);//number
console.log(valueinnumber);
console.log(valueinnumber + 3); //NaN
console.log(valueinnumber - 3); //NaN
console.log(valueinnumber * 3); //NaN
//"33" => 33
//"33abc" => NaN
//"abc33" => NaN
//true => 1
//false => 0
//null => 0
//undefined => NaN
let isLoggedIn = 1
let booleanisloggedIn = Boolean(isLoggedIn);
console.log(booleanisloggedIn); //true
console.log(typeof booleanisloggedIn); //boolean
//"0" => false
//"1" => true
//"abc" => true
//"" => false
let someValue = 15
let stringValue = String(someValue);
console.log(stringValue); //15
console.log(typeof stringValue); //string

//operaTions
// + => addition
// - => subtraction
// * => multiplication
// / => division
// % => modulus
// ** => exponentiation
// ++ => increment
// -- => decrement
// += => addition assignment
// -= => subtraction assignment
// *= => multiplication assignment
// /= => division assignment
// %= => modulus assignment
// **= => exponentiation assignment
// ++ => increment assignment
// -- => decrement assignment
// == => equality
// === => strict equality
// != => inequality
// !== => strict inequality
// > => greater than
// < => less than
// >= => greater than or equal to
// <= => less than or equal to
// && => logical and
// || => logical or
// ! => logical not
// & => bitwise and
// | => bitwise or
// ^ => bitwise xor
// ~ => bitwise not
// << => left shift

// >> => right shift
// >>> => unsigned right shift
// ? : => ternary operator
// , => comma operator
// . => member operator
// [] => array literal
// {} => object literal
// () => function literal
// => => arrow function
// ; => statement terminator
// : => label
// -> => arrow function
// => => arrow function
let value = 10
let negvalue = -value
console.log(negvalue); //-10

let str1 = "Hello"
let str2 = "World"
let str3 = str1 + " " + str2
console.log(str3); //Hello World

console.log("1" + 2); //12
console.log(1 + "2"); //12
console.log(1 + 2 + "3"); //33
console.log("1" + 2 + 3); //123
console.log(1 + 2 + "3" + 4); //334
//first if there is string it will be conactenated if string is at last operation will perfomed then concatented
//if there is string in between it will be concatenated

console.log(3+4*5%3); //5
console.log((3+4)*5%3) //2 
console.log(3+4*5/3); //9.666666666666666
console.log(true )//true
console.log(+true)//1
console.log(-true)//-1
console.log(!true)//false
console.log(!!true)//true

console.log(+""); //0
console.log(+"abc"); //NaN
console.log(+"123abc"); //NaN

let num1,num2,num3
num1=num2=num3= 2+2
console.log(num1); //4

let gamecounter =100
gamecounter ++; //post increment
console.log(gamecounter); //101
++gamecounter; //pre increment
console.log(gamecounter); //102