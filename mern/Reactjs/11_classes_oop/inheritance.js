class User {
    constructor(username) {
        this.username = username
    }
    logMe(){
        console.log(`USERNAME is ${this.username}`);
    }
}

class Teacher extends User{
    constructor(username,email,password){
        super(username) // this keyword directly takes username 
        this.email = email
        this.password = password
    }
    addCourse(){
        console.log(`A new course was added by ${this.username}`)
    }
}

const chai = new Teacher("chai","chai@gmail.com","123")
chai.addCourse()
chai.logMe()

const masalachai = new User("masalachai")
// masalachai.addCourse()
masalachai.logMe()

console.log(chai === masalachai);//false
console.log(chai == Teacher);//false
console.log(chai instanceof User);//true
console.log(chai instanceof Teacher);//true
console.log(masalachai instanceof Teacher);//false


