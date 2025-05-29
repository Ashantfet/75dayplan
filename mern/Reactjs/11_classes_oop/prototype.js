// let myName ="hitesh                    "
// console.log(myName.trim.length);

// console.log(myName.trueLength);

let myHeroes =["thor","spiderman"]

let heroPower ={
    thor : "hammer",
    spiderman : "sling",

    getSpiderPower: function(){
        console.log((`spidy Power is ${this.spiderman}`));
    }
}

Object.prototype.hitesh = function(){
    console.log("hitesh is present in all objects");
    
}
Array.prototype.heyHitesh = function(){
    console.log('hitesh says hello');
    
}
heroPower.hitesh()
myHeroes.hitesh()
//heroPower.heroPower()
myHeroes.heyHitesh()
//heroPower.heyHitesh()

//inheritance 

const User ={
    name: "chai",
    email: "google.com"
}
const Teacher ={
    makeVideo : true
}

const TeachingSupport ={
    isAvailable :false
}
const TASupport ={
    makeAssignment: 'js Assignment',
    fulltime: true,
    __proto__: TeachingSupport
}
Teacher.__proto__ =User

//modern syntax
Object.setPrototypeOf(TeachingSupport,Teacher)//prototyping inheritance

let anotherUsername = "Chaiaurcode      "
String.prototype.trueLength = function(){
    console.log(`${this}`);
    // console.log(`${this.name}`);
    console.log(`True length is ${this.trim().length}`);
    
    
}
anotherUsername.trueLength()
"hitesh".trueLength()
"iceTea".trueLength()