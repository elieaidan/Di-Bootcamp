// // Exercice 1 

// const people = ["Greg", "Mary", "Devon", "James"];

// // Partie I

// const nogreg = people.splice(0,1);
// console.log(people);

// const jason = people.splice(2,1,"Jason");
// console.log(people);

// const add = people.push("Elie");
// console.log(people);

// const indexOf = people.indexOf("Mary");

// console.log(indexOf);

// const slice = people.slice(1,4);

// console.log(slice);

// const foo = people.indexOf("foo")

// console.log(foo);

// // because "foo" isn't in the array 

// const last = people[people.length-1]

// console.log(last);

// console.log(people);


// console.log(slice);

// Partie 2


// const people = ["Mary", "Devon", "Jason", "Elie"]


// for ( x = 0; x <=3; x ++) {
//     console.log(people[x]);
    
// } 



// for ( x = 0; x <=3; x ++) {
//     console.log(people[x]);
//     if (people[x] == "Jason") break;

//  } 



//  Exercise 2

// const favoritecolors = ["Blue", "Red", "Orange", "Purpple"];

// for (x= 0 ; x <=3 ; x++){

//     // let num = favoritecolors.indexOf(favoritecolors[x]);


//     // console.log(`My #${num} choice is ${favoritecolors[x]}`);



//     console.log(`My #${x+1} choice is ${favoritecolors[x]}`)

// }


// Exercise 3 

// let number =  prompt("Choose a number");
// number = Number(number);

// while (number < 10){
//     number = prompt("Chose a number")
//     number = Number(number)

// }


// Exercise 4


// const building = {
//     numberOfFloors: 4,
//     numberOfAptByFloor: {
//         firstFloor: 3,
//         secondFloor: 4,
//         thirdFloor: 9,
//         fourthFloor: 2,
//     },
//     nameOfTenants: ["Sarah", "Dan", "David"],
//     numberOfRoomsAndRent:  {
//         sarah: [3, 990],
//         dan:  [4, 1000],
//         david: [1, 500],
//     },
// }

// const nof = building["numberOfFloors"];
// console.log(nof);


// const n1 = building["numberOfAptByFloor"]["firstFloor"];
// console.log(n1);

// const n3 = building["numberOfAptByFloor"]["thirdFloor"];
// console.log(n3);


// const name2 = building["nameOfTenants"][1];


// const nr2 = building["numberOfRoomsAndRent"]["dan"][0];




// const priceSarah = building["numberOfRoomsAndRent"]["sarah"][1];
// const priceDavid = building["numberOfRoomsAndRent"]["david"][1];
// const priceDan = building["numberOfRoomsAndRent"]["dan"][1];
// const change = building["numberOfRoomsAndRent"]["dan"];
// console.log(change);

// if (priceDavid + priceSarah < priceDan ){
//    priceDan+200

// }


// Exercice 5

// const family = {thebigger:"John", themiddle:"Rose", thesmaller:"Pat"};

// for (nom in family){
//     console.log(nom);
//     console.log(family[nom]);

// }


// Exercise 6 

// const details = {
//     my: 'name',
//     is: 'Rudolf',
//     the: 'raindeer'
//   }

// for (sentence in details){
//     console.log(sentence);
//     console.log(details[sentence]);

// }


// Exercise 7 

const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

// Un groupe d'amis a décidé de créer une société secrète.
// Le nom de la société sera la première lettre de chacun de leurs noms triés par ordre alphabétique.
// Indice : une chaîne est un tableau de lettres
// Console.log le nom de leur société secrète. La sortie doit être "ABJKPS"

const letters = ["J", "P", "S", "A", "B", "K"];

const secret = letters.sort();

const sec = secret.join('')

console.log(sec);


