// class User {
//     constructor(email,password){
//         this.email = email;
//         this.password = password
//     }
//     get email(){
//         return this._email.toUpperCase()
//     }
//     set email(value){
//         this._email = value
//     }
//     get password(){
//         return `${this._password}hitesh`
//     }
//     set password(value){
//         this._password = value.toUpperCase()
//     }

// }

// const hitesh = new User("h@gmail.com","123")
// console.log(hitesh.password);
// console.log(hitesh.email);

//getter setter using properties

// function User(email,password){
//     this._email = email;
//     this._password =password

//     Object.defineProperty(this,'email',{
//         get: function(){
//             return this._email.toUpperCase()
//         },
//         set: function(value){
//             this._email = value
//         }
//     }),
//     Object.defineProperty(this,'password',{
//         get: function(){
//             return this._password.toUpperCase()
//         },
//         set: function(value){
//             this._password = value
//         }
//     })
// }

// const chai = new User("chai@vchai.com","chai")
// console.log(chai.email);

//Object based get set

const User = {
    _email : "h@hc.com",
    _password : "abc",

    get email(){
        return this._email.toLocaleUpperCase()
    },
    set email(value){
        this._email = value
    }
}

const tea = Object.create(User)
console.log(tea.email);
