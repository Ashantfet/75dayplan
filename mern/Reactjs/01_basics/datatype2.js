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