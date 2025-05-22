const name ="Ashant"; //string
const repocount = 20
console.log(name+repocount+" value")
//string interpolation
console.log(name + " " + repocount + " value") //string concatenation
console.log(name.concat(repocount)) //string concatenation
console.log(`Hello my name is ${name} and I have ${repocount} repositories`); //template literals``;
const gameName = "Call of -Duty"
const game = new String(gameName) //string object
console.log(game) //String { 'Call of Duty' }
console.log(gameName)
console.log(game[0]) //C
console.log(game.charAt(0)) //C
console.log(gameName.__proto__) //String {}
console.log(game.__proto__) //String {}

console.log(gameName.length) //12
console.log(game.length) //12
console.log(gameName.toUpperCase()) //CALL OF DUTY
console.log(game.toUpperCase()) //CALL OF DUTY
console.log(gameName.toLowerCase()) //call of duty
console.log(game.toLowerCase()) //call of duty
console.log(gameName.indexOf("a")) //1
console.log(game.indexOf("a")) //1

const newString = gameName.substring(0,4) //Call
console.log(newString) //Call   it includes 0and excludes 4 it can take negative value too

const newstring1 = gameName.slice(0,4) //it does not allow negative value
console.log(newstring1) //Call

const string1 = "   Hello World   "
console.log(string1) //   Hello World
console.log(string1.trim()) //Hello World
console.log(string1.trimStart()) //Hello World
console.log(string1.trimEnd()) //   Hello World it works on only new line

const url = "https://www.google.com"
const url1 = "https://www.google.com/%20ashant"

console.log(url1.replace('%20','-'))
console.log(url1.includes('ashant'))//true

console.log((gameName.split('-')));
