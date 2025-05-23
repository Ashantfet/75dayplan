// singleton  - single instance of an object using constructors
//Object.create({}) // empty object

// const tinderuser = new Object() //singleton object
const tinderuser = {} //empty object non-singleton object
tinderuser.id ="123abc"
tinderuser.name = "shera"
tinderuser.isloggedin = false



console.log(tinderuser);

const regularUser = {
    email : "sohan@gmail.com",
    fullname : {
        userfullname: "Ashant",
        lastname: "kumar"
    }
}
console.log(regularUser.fullname.lastname)// ? is used to access if that particular object not found

const obj1 = {1:"a",2:"b"}
const obj2 = {3:"c",4:"d"}
const obj4 = {5:"c",6:"d"}
//const obj3 = {obj1,obj2} //{ obj1: { '1': 'a', '2': 'b' }, obj2: { '3': 'c', '4': 'd' } }
//const obj3 =Object.assign(obj1,obj2) //{ '1': 'a', '2': 'b', '3': 'c', '4': 'd' }
//const obj3 =Object.assign({},obj1,obj2,obj4)//const obj2 = {3:"c",4:"d"} // empty grid is given to make it source

const obj3 ={...obj1, ...obj2}
//console.log(obj3);

const users = [
    {
        id : 1,
        email : "a@gmail.com"
    },
        {
        id: 2,
        email : "h@gmail.com"
    },
        {
        id: 3,
        email : "n@gmail.com"
    }
]

console.log(users[1].email)
console.log(Object.keys(tinderuser));
console.log(Object.values(tinderuser));
console.log(Object.entries(tinderuser));

console.log(tinderuser.hasOwnProperty('isloggedin'));



