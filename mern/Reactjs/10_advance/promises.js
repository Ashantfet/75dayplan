//fetch(('https://something.com')).then().catch().finally()

//making of promises

const promniseOne = new Promise(function(resolve,reject) {
    //DO an async task
    //DB calls cryptography network
    setTimeout(function(){
        console.log('Async Task is completed.');
        resolve()
    },1000)
})

promniseOne.then(function(){
    console.log('Prosmise consumed')
})

new Promise(function(resolve,reject){
    setTimeout(function(){
        console.log("Async task 2");
        resolve()
    },1000)
}).then(function(){
    console.log("Async 2 Resolved")
})

const promiseThree = new Promise(function(resolve,reject){
    setTimeout(function(){
        resolve({username:"chai",email:"chai@gmail.com"})
    },1000)
})
promiseThree.then(function(user){
    console.log(user);
})

const promiseFour = new Promise(function(resolve, reject){
    setTimeout(function(){
        let error =true
        if(!error){
            resolve({username:"hitesh",password:"123"})
        }else{
            reject('Error: Something went wrong')
        }
    },1000)
})

promiseFour.then((user)=> {
    console.log(user);
    return user.username
}).then((username)=>{
    console.log(username);
    
}).catch(function(error){
    console.log(error);
    
}).finally(()=> console.log("The promise is either resolved or rejected"))


const promiseFive = new Promise(function(resolve,reject){
        setTimeout(function(){
        let error =true
        if(!error){
            resolve({username:"Javascript",password:"123"})
        }else{
            reject('Error: JS went wrong')
        }
    },1000)
})
async function ConsumePromiseFive(){
    try {
        const response = await promiseFive
        console.log(response);
    } catch (error) {
        console.log(error);
    }
    

}
ConsumePromiseFive()

// async function getAllUsers(){
//     try {
//          const response = await fetch('https://jsonplaceholder.typicode.com/users')
//         console.log(response);
        
//         // const data = response.json()
//         // console.log(data);
//     } catch (error) {
//         console.log("E: ",error);
        
//     }
// }

// getAllUsers()

fetch('https://api.github.com/users/hiteshchoudhary')
.then((response) => {
    return response.json()
})
.then((data)=>{
    console.log(data);
    
})