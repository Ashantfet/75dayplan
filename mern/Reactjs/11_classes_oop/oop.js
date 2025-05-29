//OBJECT LITERAL
const user ={
    username : "Ashant",
    loginCount: 8,
    signedIn: true,

    getUserDetails: function(){
        //console.log("Gt user details from database.");
        //console.log(`Username: ${this.username}`);
        console.log((this));
        
    }
}

// const user2 ={
//     username : "Ashant",
//     loginCount: 8,
//     signedIn: true,

//     getUserDetails: function(){
//         //console.log("Gt user details from database.");
//         //console.log(`Username: ${this.username}`);
//         console.log((this));
        
//     }
// }  //we have to make for every user

// console.log(user.username);
// console.log(user.getUserDetails());
//console.log((this)); {}

//constructor function

//const promiseOne = new Promise()
const date = new Date()  //new context used to make using new keyword called as constructor function

function User(username,loginCount,isLoggedIn){
    this.username = username;
    this.loginCount =loginCount;
    this.isLoggedIn = isLoggedIn
    this.greeting =function(){
        console.log(`welcome ${this.username}`);
        
    }

    return this
}

const userOne = new User("Ashant",23,true)
const userTwo = new User("ChaiAurCoe",12,true) // we can see without new keyword it is overwriting previous one 
console.log(userOne.constructor);
// console.log(userTwo);

//new keyword creates a new instance 
//a constructor function is called
//every data is injected inside the new instance
//we can see different data 

