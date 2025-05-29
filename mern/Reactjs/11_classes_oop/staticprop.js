class User{
    constructor(username){
        this.username = username
    }
    logMe(){
        console.log(`Username: ${this.username}`);
    }
    static createId(){   // without static keyword it allows everyone make id or generate id
        return `123`
    }
}
const Ashant = new User("Ashant")
//console.log(Ashant.createId());

class Teacher extends User{
    constructor(username,email){
        super(username)
        this.email = email
    }
}
 const iphone = new Teacher("iphone","i@gamil.com")
iphone.logMe()
//console.log(iphone.createId()); //not allowed for children too
