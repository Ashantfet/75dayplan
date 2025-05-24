//scope
let a=300 //global scope
const b = 400 //global scope
if(true){
let a =10
const b = 20          //block scope
var c = 30
console.log("Inner block",a); // 10

}


//console.log(a);
console.log(a);// 300

//console.log(b);
console.log(c); // var is function scope but still accessible outside the block
//{} it used for scope in functions

//function scope

//global scope using program and console is different

//nothing should be leaked from one function to another or from one block scope

function one() {
    const username ="ashant"
    function two() {
        const password = "1234"
        console.log(username);
    }
    //console.log(password); //undefined //not accessible
    two()
}
one()

if(true){
    const username = "ashant"
    if(true){
        const password = "1234"
        console.log(username + password);
    }

    //console.log(password)  //not accessible
}

//console.log(username); //not accessible

//++++++++++++++++++++++++++++++++++++++++++++++++++++++ interesting part +++++++++++++++++++++++++++++++
console.log(addone(5)) // function declaration;
//console.log(addTwo(5)) // function expression; this results in error due to storing function in a variable (hoisting )

function addone(num1){
    return num1 + 1
    
}
const addTwo = function(num1){
    return num1 + 2
}

addTwo(10) // function expression
console.log(addone(10))
console.log(addTwo(10))

