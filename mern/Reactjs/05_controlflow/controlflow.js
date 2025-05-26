//if 
if (true) {
    console.log("This is true");
}

// const isUserLoggedIn = true; //operator assignment
// if (isUserLoggedIn) {
//     console.log("User is logged in");
// }

// < ,>, <=, >=, ==, !=, ===(type checking), !==, 

if(2==="2") {
    console.log("2 is equal to 2");
}
const temperature = 17;

if (temperature > 40) {
    console.log("It's a hot day");
}
else if (temperature < 20) {
    console.log("It's a cold day");
}
else {
    console.log("It's a lovely day");
}

const score = 200
if (score >= 100) {
    const PowerLevel = "Pro";
    console.log("You are a " + PowerLevel + " gamer");
    // Template literals
    console.log(`You are a ${PowerLevel} gamer`);

}
else if (score >= 50) {
    console.log("You are a good gamer");
}
else if (score >= 20) {
    console.log("You are a beginner gamer");
}

//console.log(`You are a ${PowerLevel} gamer`);

 const balance = 1000;
// if (balance>=500) console.log("test");

// if (balance < 500) {
//     console.log("You are low on balance");
// }
// else if (balance < 1000) {
//     console.log("You are low on balance, but you can still make a transaction");
// }
// else if (balance < 2000) {
//     console.log("You have a good balance");
// }

const isUserLoggedIn = true;
const debitcard =true;
const isloggedInfromemail = true;
const isloggedInfromphone = true;
if (isUserLoggedIn && debitcard && balance >= 500) {
    console.log("You can make a transaction");
}

if (isloggedInfromemail || isloggedInfromemail || balance >= 500) {
    console.log("User Logged in successfully");
}

// switch (key) {
//     case value:
        
//         break;

//     default:
//         break;
// }


const month =3
switch (month) {
    case 1:
        console.log("January");
        break;
    case 2:
        console.log("February");
        break;
    case 3:
        console.log("March");
        break;
    case 4:
        console.log("April");
        break;
    case 5:
        console.log("May");
        break;
    case 6:
        console.log("June");
        break;
    case 7:
        console.log("July");
        break;
    case 8:
        console.log("August");
        break;
    case 9:
        console.log("September");
        break;
    case 10:
        console.log("October");
        break;
    case 11:
        console.log("November");
        break;
    case 12:
        console.log("December");   //ctrl + d to duplicate line
        break;

    default:
        console.log("Invalid month");    //without break it will continue to execute the next case but default will not execute without break;
        break;  
}

const UserEmail = [] 

if(UserEmail) {
    console.log("User email is present");
}
else {
    console.log("User email is not present");
}

//falsy values :  false,0,-0,BigInt (0n), "", null, undefined, NaN

//truthy values: true, 1,-1,"0","false"," ",[],{},function(){},Symbol(),BigInt(1),Infinity,-Infinity    

if (UserEmail.length===0) {
    console.log("Array is empty");
}
else {
    console.log("Array is not empty");
}

const emptyObj = {};
if (Object.keys(emptyObj).length === 0) {
    console.log("Object is empty");
}
else {
    console.log("Object is not empty");
}

//Nullish Coalescing Operator (??) - it will return the first value if it is not null or undefined, otherwise it will return the second value

let val1;
//val1 = 5??10             //5
//val1 = null ?? 10;      //10
//val1 = undefined ?? 10;  //10
val1 = null??10??20;  //10

console.log(val1); // 5

// Ternary Operator

//condition ? expressionIfTrue : expressionIfFalse;   

const iceTeaPrice = 50;
const isIceTeaAvailable = true;

iceTeaPrice < 10 ? console.log("Ice Tea is available") : console.log("Ice Tea is not available");

