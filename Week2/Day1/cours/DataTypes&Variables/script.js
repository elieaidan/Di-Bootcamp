// same data in variables
let myProfileInFacebook; //CAMEL CASE

// let keyword

let myNumber = 23;
// console.log(myNumber); //23

// a variable called myNumber that is equal to 23
// the value of te variable is 23
// 23 is a number

let pet = "cat";
// console.log(pet); //"cat" - the value of the variable
// console.log("pet"); //"pet" - a string with the value pet

// Change the value
pet = "dog";
// console.log(pet); //dog

// constant variables - cannot redefine them

const johnAge = 23;
const johnName = "John";
const johnPet = "rabbit";

console.log(johnAge);

// johnAge = 54; //error : cannot change the constant variable

//DECLARATION
//DEFINITION

let computer = "Mac";
//I declare the variable, and define it with the value Mac

let day;
// I declare the variable day

day = "Sunday";
// I define the variable to "Sunday"

let friend = "John";
friend = "Tom"; //redefining the variable

let time = 12;

// VARIABLE, that is a string that is equal to a sentence
// "John and Tom are working on Sunday"

const sentence = "John and Tom are working on Sunday at 12pm";

// CONCATENATION
const sentenceOne = "John and " + friend + " are working on " + day + " at " +  time + "pm";
console.log(sentenceOne);

// Template literals backtick : RECOMMENDED
const sentenceTwo = `John and ${friend} are working on ${day} at ${time}pm`;
console.log(sentenceTwo);



// a constant variable needs to be declared & defined at the same time
// const taxes; // error 
