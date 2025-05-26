// const coding = ["js", "python", "java", "c++", "ruby"];
// const values =coding.forEach((item ) => {
//     //console.log(`Item: ${item}`);
//     return item
// })

// console.log(values); // undefined, forEach does not return anything

const numbers = [1, 2, 3, 4, 5];
// const newnums = numbers.filter((num) => {
//     return num > 2; // Filter numbers greater than 2
// })  

// const newnums =[]
// numbers.forEach((num) => {
//     if (num > 2) {
//         newnums.push(num); // Push numbers greater than 2 into newnums
//     }
// });
// console.log("Filtered numbers:", newnums); // Log the filtered numbers


const books =[
    { title: "Book A", author: "Author A", price: 10 },
    { title: "Book B", author: "Author B", price: 15 },
    { title: "Book C", author: "Author C", price: 20 },
    { title: "Book D", author: "Author D", price: 25 }
]

const userBooks =books.filter((bk) => bk.price > 15) // Filter books with price greater than 15
const userBooks1 = books.map((bk) => {bk.author = "New Author"; return bk;}) // Map to change author of each book
console.log("Filtered books:", userBooks); // Log the filtered books
console.log("Mapped books:", userBooks1); // Log the mapped books with new authors
console.log(userBooks);


const myNumbers = [1,2,3,4,5,6,7,8,9,10];

//const newNums = myNumbers.map((num) => num+10)
 const newNums = myNumbers
                    .map((num) => num *10)
                    .map((num) => num + 5)
                    .filter((num) => num >= 40)

console.log((newNums));

//reduce example

const mynums = [1,2,3]
// const myTotal = mynums.reduce(function (acc,currval){
//     console.log("Accumulator:", acc, "Current Value:", currval);
    
//     return acc +currval
// },0)

const myTotal = mynums.reduce((acc, currVal) => acc + currVal, 0); // Reduce to calculate the total sum of the numbers
console.log("Total:", myTotal); // Log the total sum of the numbers

const shoppingCart = [
    { item: "Apple", price: 1.5, quantity: 3 },
    { item: "Banana", price: 0.5, quantity: 6 },
    { item: "Orange", price: 2, quantity: 2 }
];
const totalCost = shoppingCart.reduce((acc, currItem) => {
    console.log("Accumulator:", acc, "Current Item:", currItem);
    return acc + (currItem.price * currItem.quantity); // Calculate total cost by multiplying price and quantity
}, 0);
console.log("Total Cost:", totalCost); // Log the total cost of the shopping cart
