// dates
let mydate = new Date(); //current date
console.log(mydate); //2023-10-05T07:23:45.000Z
console.log(mydate.toString()); //Thu Oct 05 2023 07:23:45 GMT+0000 (Coordinated Universal Time)
console.log(mydate.toDateString()); //Thu Oct 05 2023
console.log(mydate.toTimeString()); //07:23:45 GMT+0000 (Coordinated Universal Time)
console.log(mydate.toLocaleString()); //10/5/2023, 7:23:45 AM
console.log(mydate.toLocaleDateString()); //5/22/2025
console.log(typeof mydate); //object

let mycreatedate = new Date("2023-10-05"); //date
console.log(mycreatedate.toDateString()); //Thu Oct 05 2023

let mydate1 = new Date(2025,22,5 ,16,12,12);
console.log(mydate1); //2026-10-05T16:12:12.000Z

let mytimestamp = Date.now(); //timestamp
console.log(mytimestamp); //1696490600000  in ms
console.log(mycreatedate.getTime()); //1696490600000   in ms
console.log(Math.floor(Date.now()/1000));

console.log(mydate.getMonth()+1); //9 0-11

console.log(mydate.toLocaleString('default',{weekday: "long"})) //Thursday
console.log(mydate.toLocaleString('default',{month: "long"})) //October
console.log(mydate.toLocaleString('default',{year: "numeric"})) //2023