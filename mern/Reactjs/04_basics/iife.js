//immediately invoked function expression

(function chai() {
    //named iife
    console.log("DB connected");
})();
//sometimes ; becomes necessary to avoid errors in some cases
( (name)=> {
    console.log(`DB connected TWO ${name}`);
})('ashant'); // IIFE with parameter