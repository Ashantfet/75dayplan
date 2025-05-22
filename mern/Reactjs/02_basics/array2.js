const marvel_heroes = ["thor", "ironman", "hulk", "spiderman", "black widow"];
const dc_heroes = ["batman", "superman", "wonderman", "flash", "aquaman"];

//marvel_heroes.push(dc_heroes); //add to the end
// console.log(marvel_heroes); // [ 'thor', 'ironman', 'hulk', 'spiderman', 'black widow', [ 'batman', 'superman', 'wonderman', 'flash', 'aquaman' ] ]
//it adds whole array to the end ie takes it as a single element
//console.log(marvel_heroes[5][0]); //batman
const allheroes =marvel_heroes.concat(dc_heroes) //add to the end
//console.log(marvel_heroes); // [ 'thor', 'ironman', 'hulk', 'spiderman', 'black widow']
//console.log((allheroes));
//... spread operator it spreads the array elements
const all_new_heroes = [...marvel_heroes, ...dc_heroes] //add to the end
console.log(all_new_heroes); // [ 'thor', 'ironman', 'hulk', 'spiderman', 'black widow', 'batman', 'superman', 'wonderman', 'flash', 'aquaman' ]
console.log(marvel_heroes); // [ 'thor', 'ironman', 'hulk', 'spiderman', 'black widow' ]

const arr2 = [1,2,3,[4,5,6],7,[8,11],9,10]
const realarr2 = arr2.flat(Infinity) //flatten the array  it goes to all the depths
console.log(realarr2); // [ 1, 2, 3, 4, 5, 6, 7, 8, 11, 9, 10 ]

console.log(Array.isArray(arr2)) //check if it is an array
console.log(Array.from("hello")) //convert string to array
console.log(Array.from({name: "Ashant", age: 23})) //convert object to array   //interesting array it must have defined both

let score = 100
let score1 = 200
let score2 = 300
let score3 = 400
let score4 = 500
console.log(Array.of(score, score1, score2, score3, score4)) //convert variables to array
console.log(Array.of(1,2,3,4,5)) //convert variables to array;
