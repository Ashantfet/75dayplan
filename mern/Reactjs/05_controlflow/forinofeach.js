// //for of

// const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
// const evenNumbers = numbers.filter((number) => number % 2 === 0); // Filter even numbers from the array

// for (const element of evenNumbers) {
//     console.log("Element:", element);
    
// }

// const greetings = ["Hello", "Hi", "Hey", "Hola", "Bonjour"];
// const longGreetings = greetings.filter((greeting) => greeting.length > 3); // Filter greetings longer than 3 characters
// for (const greeting of longGreetings) {
//     console.log("Greeting:", greeting);
    
// }
//maps
// const map = new Map();
// map.set("name", "John");
// map.set("age", 30);
// map.set("city", "New York");
// console.log(map); // Log the entire map
// for (const [key, value] of map) {
//     console.log(`Key: ${key}, Value: ${value}`);
    
// }

const myObject = {
    name: "Alice",
    age: 25,
    city: "Los Angeles" 
}

for (const key in myObject) {
    console.log(`${key} : ${myObject[key]}`);
    
}

const programming =["JavaScript", "Python", "Java", "C++", "Ruby"];
const filteredProgramming = programming.filter((lang) => lang.length > 5); // Filter languages longer than 5 characters
for(const key in programming) {
    console.log(`Programming Language: ${programming[key]}`);
    
}

// const map = new Map();
// map.set("name", "John");
// map.set("age", 30);
// map.set("city", "New York");

// for(const key in map) {
//     console.log(`Key: ${key}, Value: ${map[key]}`);
    
// }      //not woeking with map

//for each loop
const coding =["js", "python", "java", "c++", "ruby"];
// coding.forEach((language, index) => {
//     console.log(`Language at index ${index}: ${language}`);
// });

coding.forEach( function(val){
    console.log(`Language: ${val}`);
})


// coding.forEach((item) => {
//     console.log(`Item: ${item}`);
// })

function printMe(item) {
    console.log(`Item: ${item}`);
}
coding.forEach(printMe); // Using a named function to print each item

// coding.forEach((item, index,arr) => {
//     console.log(`Item: ${item}, Index: ${index}, Array: ${arr}`);
// });

const myCoding = [
    {
    languageName :"javaScript",
    languageFileName : "js"
    },
    {
    languageName : "Python",
    languageFileName : "py"
    },
    {
    languageName : "java",
    languageFileName : "java"
    }
]

myCoding.forEach((item, index) => {
    console.log(`Language Name: ${item.languageName}, File Name: ${item.languageFileName}, Index: ${index}`);
});