
function sayMyname(){
console.log("A");
console.log("s");
console.log("h");
console.log("a");
console.log("n");
console.log("t");

}

//sayMyname()

function add2no(no1,no2){
    //no1,no2 are parameters
    // let result =no1 +no2
    // return result
    // console.log(no1+no2);

    return no1+no2
}
const result = add2no(3,5)//3,5 are argument
console.log("Result: ",result);

function loginuserMessage (username= "sam"){
    if(!username ){
        console.log("please enter a username");
        return
    }
    return `${username} just logged in`
} 
console.log(loginuserMessage("Ashant"));// if no value passed it becomes undefined
console.log(loginuserMessage());