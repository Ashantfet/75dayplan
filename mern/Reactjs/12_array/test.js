// const myArr =[]
// %DebugPrint(myArr)

//Continious, Holey array
//SMI (small integer)
//packed element
//double(float,string,function)

//array -> elements

const arrTWO = [1,2,3,4,5]  //PACKED_SMI_ELEMENTS

arrTWO.push(6.0) //PACKED_DOUBLE_ELEMENTS
arrTWO.push('7') //PACKED_ELEMENTS

arrTWO[10] =11
//  HOLEY_ELEMENTS
console.log(arrTWO);
console.log(arrTWO.length);
console.log(arrTWO[9]);//HOLEY_ELEMENTS //CHECKS hasOwnProperty(arrTwo,9)
//hasOwnProperty(arrTwo.prototype,10)
//hasOwnProperty(Object.prototype,10)  //if holes these three checks are used
//BOUND  CHECK
console.log(arrTWO[19]);
//holes are very expensive in js

const arrThree =[1,2,3,4,5]
console.log(arrThree[4]);
//SMI > DOUBLE >PACKED
//H_SMI > H_DOUBLE >H_PACKED

//TOTAL 30 VARIATION 
//ONCE DOWNGRADED IT CANNOT BE UPGRADED
//

const arrFour = new Array(3)

//just 3 holes. HOLEY_SMI_ELEMENTS
arrFour[0] ='1' //HOLEY_ELEMENTS
arrFour[1] ='1' //HOLEY_ELEMENTS
arrFour[2] ='1' //HOLEY_ELEMENTS

//it can be bettered
const arrFive =[]
arrFive.push('1') //PACKED_ELEMENTS
arrFive.push('2') //PACKED_ELEMENTS
arrFive.push('3') //PACKED_ELEMENTS

const arrSix =[1,2,3,4,5]
arrSix.push(Infinity) //PACKED_DOUBLE

//for, for-of,forEach  use of default methods are suggesated


