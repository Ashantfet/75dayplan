//array it's size can be resizeable 


const myarr = [1,2,3,true, "Ashant", null, undefined, {name: "Ashant"}, [1,2,3], function() {console.log("Hello World")}, Symbol("I am a symbol")]; //array
console.log(myarr); // [ 1, 2, 3, true, 'Ashant', null, undefined, { name: 'Ashant' }, [ 1, 2, 3 ], [Function], Symbol( I am a symbol ) ]
console.log(myarr[0]); //1
//copy operation -swallow copy keeps same refrence point  while deep copy creates a new refrence point
//swallow copy
const myarr1 = myarr; //swallow copy
console.log(myarr1); // [ 1, 2, 3, true, 'Ashant', null, undefined, { name: 'Ashant' }, [ 1, 2, 3 ], [Function], Symbol( I am a symbol ) ]
console.log(myarr1[0]); //1

const myarr2 = new Array(1,2,3,4)
console.log(myarr2); // [ 1, 2, 3, 4 ]
//array methods

myarr.push(100) //add to the end
myarr.push(200) //add to the end
console.log(myarr); // [ 1, 2, 3, true, 'Ashant', null, undefined, { name: 'Ashant' }, [ 1, 2, 3 ], [Function], Symbol( I am a symbol ), 100 ]
myarr.pop() //remove from the end
console.log(myarr); // [ 1, 2, 3, true, 'Ashant', null, undefined, { name: 'Ashant' }, [ 1, 2, 3 ], [Function], Symbol( I am a symbol ) ]

myarr.unshift(0) //add to the beginning
console.log(myarr); // [ 0, 1, 2, 3, true, 'Ashant', null, undefined, { name: 'Ashant' }, [ 1, 2, 3 ], [Function], Symbol( I am a symbol ) ]
myarr.shift() //remove from the beginning
console.log(myarr); // [ 1, 2, 3, true, 'Ashant', null, undefined, { name: 'Ashant' }, [ 1, 2, 3 ], [Function], Symbol( I am a symbol ) ]

console.log(myarr.includes(1)); //true
console.log(myarr.indexOf(false)); //-1

const newArr = myarr2.join()
console.log(myarr2)
console.log(typeof newArr); //1,2,3,true,Ashant,,undefined,[object Object],[object Object],[Function],Symbol( I am a symbol )

//slice and splice
console.log("A",myarr2);
const newArr1 = myarr2.slice(0, 2) //slice does not change the original array
console.log("B",myarr2); // [ 1, 2, 3, 4 ]
console.log(newArr1); // [ 1, 2 ]
const newArr2 = myarr2.splice(0, 2) //splice changes the original array
console.log("C",myarr2); // [ 3, 4 ]
console.log(newArr2); // [ 1, 2 ]
