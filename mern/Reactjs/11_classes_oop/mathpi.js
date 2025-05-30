const descriptor = Object.getOwnPropertyDescriptor(Math,"PI")
console.log(descriptor);// due to it is set as {
//   value: 3.141592653589793,
//   writable: false, // no writable allowed directly into its engine
//   enumerable: false,
//   configurable: false
// }


// console.log(Math.PI);
// Math.PI =5
// console.log(Math.PI); //it does not allow to update the value of it


const chai = {
    name: 'ginger chai',
    price : 250,
    isavailabe: true,
    orderChai: function(){
        console.log("chai nhi bani");
        
    }
}

console.log(Object.getOwnPropertyDescriptor(chai,"name"));
Object.defineProperty(chai,'name',{
    //writable:false,
    enumerable:true
})
// console.log(Object.getOwnPropertyDescriptor(chai,"name"));

for (let [key,value] of Object.entries(chai)){
    if(typeof value!=='function'){
        console.log(`${key} : ${value}`);
    }
}

