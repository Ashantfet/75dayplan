
// object literals

const mysym = Symbol("my symbol")

const person ={
    name :"Ashant kumar",
    [mysym]: "my symbol",//correct way to use symbol in object never use without bracket
    age: 23,
    location: "India",
    email: "ashant@gmail.com",
    isloggedin: true
}

//myArray =["hello", "world"]
//console.log(person."full name") // Ashant not allowed
//console.log(person.full name) // Ashant not allowed
//console.log(person["full name"]) // Ashant
console.log(person[mysym])
person.email = "ashant@iittp.ac.in"
//Object.freeze(person) // it will not allow to change it
person.email ="ashant@gkv.ac.in"
console.log(person);

person.greeting = function () {
    console.log("Hello Ashant");
}
person.greeting2 = function () {
    console.log(`Hello dear,${this.name}`);
}
console.log(person.greeting()); //without () [Function (anonymous)]
console.log(person.greeting2()); 
//mostly object is accessed using . but some of it is accessed using [] bracket