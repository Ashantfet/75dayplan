//javascript execution context

// Execution context is the environment in which JavaScript code is executed.
// It consists of the global execution context and function execution contexts.
// The global execution context is created when the JavaScript code is executed.
// Each function execution context is created when a function is called.

//global execujtion context
//function execution context
//eval execution context
//[{}] <- memory creation phase  
// execution phase

let val1=10
let val2=20

function addTwo(num1, num2) {
    let result = num1 + num2
    return result
}
let result1 = addTwo(val1, val2) // function execution context
let result2 = addTwo(100, 200) // function execution context
console.log(result2); // 300
//1) global execution ->this
//2) memory phase val1, val2, addTwo, result, result1, result2
//addnum -> defination and all other are undefined
//3) execution phase -> this is where the code is executed val1 val2 will be allocated to memory with 10 and 20
//addnum will create its own execution context
//new variable environment + execution thread
//for every function execution context, a new variable environment is created where memory phase and execution phase is createdand run for every function
//4) function execution context -> addTwo
//final total will be returned to the global execution context
//5) result1 will be assigned to the value returned by addTwo
//once it is cpompleted, it will be removed from the memory
//6) once the function is executed, it will be removed from the memory

//7) once the global execution context is completed, it will be removed from the memory
//8) once the code is executed, it will be removed from the memory

//again whole run for addTwo(100, 200)
//9) result2 will be assigned to the value returned by addTwo
//10) once the function is executed, it will be removed from the memory


//call stack
//call stack is a data structure that keeps track of function calls in JavaScript
// it is a stack data structure that follows the Last In First Out (LIFO) principle
// it is used to keep track of function calls and their execution contexts
// when a function is called, it is added to the call stack
// when the function execution is completed, it is removed from the call stack
// the call stack is used to keep track of the execution context of each function

