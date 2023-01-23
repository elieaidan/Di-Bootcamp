// Exercice 1

let x = 10;
let y = 6;

if(x>y){

    console.log("x is a biggest number");


} else {
    
    console.log("y is a biggest number ");


}


// Exercice 2

const newDog = "Chihuahua"

console.log(newDog.length);

console.log(newDog.toLowerCase());

console.log(newDog.toUpperCase());




if(newDog === "Chihuahua"){

    console.log("I love Chihuahuas, it’s my favorite dog breed");


} else {
    
    console.log("I dont care, I prefer cats");

}


// Exercice 3

// const number = prompt(`Choose a number`);
// console.log(number);




// if (number % 2 == 0) {

//     console.log("x is an even number");


// } else {
    
//     console.log("x is an odd number");

// }



// Exercice 4

const users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
const nbr = users.length
const ex= nbr-2


if (nbr === 0 ) {

    console.log(`no one is online`);


} else if (nbr === 1 ){
    
    console.log(`${users} is online`);

} else  if (nbr === 2 ){
    
    console.log(`${users[0]} and ${users[1]} is online`);

}else if (nbr >= 3 ){
    
    console.log(`${users[0]}, ${users[1]} and ${ex} is online`);

}

