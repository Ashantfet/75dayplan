const user = {
    username: "ashant",
    price: 999,
    welcomeMessage: function () {
        console.log(`Welcome ${this.username} to the world of programming`);//this regfers to current object
        console.log(this)
    }
}

user.welcomeMessage() // this refers to the current object
user.username = "sam"
user.welcomeMessage() // this refers to the current object
//console.log(this); //{} empty object refers to global object

function chai(){
    let username = "ashant" // not used by this
    console.log(this.username); // {} empty object refers to global object
    
}

chai()

const chai2 = function(){
    let username = "ashant" // not used by this
    console.log(this.username); // {} empty object refers to global object
}
chai2()

const chai3 = () => {
    let username = "ashant" // not used by this
    console.log(this.username); // {} empty object refers to global object
}
chai3()

// In arrow functions, 'this' does not refer to the current object, it refers to the global object
// In regular functions, 'this' refers to the current object
// In function expressions, 'this' refers to the current object

const addTwo = (num1, num2) => {
    return num1 + num2               //basic arrow function
}
const addTwo2 = (num1, num2) => (num1 + num2) // concise arrow function when {} return must be used otherwise it takes return implicitly

const addTwo3 = (num1, num2) => ({username: "ashant", price: 999}) // concise arrow function with object return
const addThree = (num1, num2, num3) => {
    return num1 + num2 + num3
}
console.log(addTwo3(10, 20));

const myNewArray = [2,3,4,5,6,7,8,9,10]
//myNewArray.forEach(()=> {})
