// for


// for (let index = 0; index < 10; index++) {
//     const element = index;
//     if(element ==5){
//         console.log("5 is good number");
        
//     }
//     console.log(element);
// }  //initialization comparison then increment

// for (let index = 0; index <= 10; index++) {
//     console.log("Outer loop index:", index);
    
//     for (let j = 0; j <= 10; j++) {
//         const element = j
//         //console.log("Inner loop element:", element);
//         console.log(index + '*' + j + '=' + (index * j));
//     }
//     console.log("End of inner loop for index:", index);
//     console.log("====================================");
    
// }

// let myArray = ["flash", "samsung", "nokia", "apple", "oneplus"];
// for (let index = 0; index < myArray.length; index++) {
//     const element = myArray[index];
//     console.log("Element at index", index, "is", element);
// }

//
for (let index = 0; index < 20; index++) {
    const element = index % 2 === 0 ? "even" : "odd"; // Ternary operator to check if the index is even or odd
    if(index % 3 === 0){
        console.log("Index", index, "is divisible by 3");
        continue;
    }
    if(index == 10){
        console.log("Reached index 10, breaking the loop.");
        break; // Break the loop when index is 10   
        
    }
    console.log("Element at index", index, "is", element);
    
    
}