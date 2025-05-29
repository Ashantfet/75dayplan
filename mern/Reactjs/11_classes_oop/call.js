function SetUsername(username){
    //complex DB calls
    this.username = username
    console.log("called");
    
}

function cretaeUser(username,email,password){
    SetUsername.call(this,username) //works like self in python
    this.email =email
    this.password = password
}

const chai = new cretaeUser("chai","chai@fb.com","123")
console.log(chai);
