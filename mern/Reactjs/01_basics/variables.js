//console.log("Hello World");
// This is a single line comment
const accountId = 1234567890; // This is a number    cannot be changed
const accountName = "Ashant"; // This is a string cannot be changed
let accountEmail = "ashant@gmail.com"; // This is a string
var accountPassword ="123456"; // This is a string
accountCity = "Delhi"; // This is a string
let accoutstate; //undefined 
// accountId = 234       //not allowed
// accountName = "John" //not allowed
console.log(accountCity); 
// `let` allows you to reassign values, but you cannot redeclare it in the same scope.
// `const` means the variable value cannot be reassigned and cannot be redeclared.
// `var` allows reassignment and redeclaration, but it is **not recommended** due to function-scoping and hoisting issues.

 accountEmail = " as@gmail.com"//allowed
accountPassword = "1234567" //allowed
 accountCity = "Mumbai" //allowed

console.table({accountId, accountName,accountEmail, accountPassword, accountCity, accoutstate});  