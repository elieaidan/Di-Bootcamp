
// exercise 1


const favoritefood = "pizza";
console.log(favoritefood);

const favoritemeal = "dinner";

const sentenceone = `I eat ${favoritefood} at every ${favoritemeal}`;

console.log(sentenceone);

// exercise 2

// Part 1

const myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];

const myWatchedSeriesLength = myWatchedSeries.length;

console.log(myWatchedSeries);

const myWatchedSeriesSentence = `${myWatchedSeries[0]}, ${myWatchedSeries[1]}, ${myWatchedSeries[2]}`;

console.log(myWatchedSeriesSentence);

const sentenceTwo =  `I watched 3 series : ${myWatchedSeriesSentence}`;

console.log(sentenceTwo);

// Part 2

myWatchedSeries.splice(2,1,"friends");



myWatchedSeries.push("fauda");



myWatchedSeries.splice(0, 0, "Walking Dead");



myWatchedSeries.splice(1, 1);



console.log(myWatchedSeries[1][2]);

console.log(myWatchedSeries);






// exercise 3


const celsiustemperature = 20;
const fahrenheit= celsiustemperature/5*9+32;

// console.log(fahrenheit); 

const sentencethree = `${celsiustemperature}°C is ${fahrenheit}°F.`;
console.log(sentencethree);








// exercise 4

let c;
let a = 34;
let b = 21;

console.log(a+b) //first expression
// Prediction: It will output 55, because 34 and 21 are numbers.
// Actual:55

a = 2;

console.log(a+b) //second expression
// Prediction: It will output 23, because 2 and 21 are numbers.
// Actual:23

// What is the value of c?
// console.log(c);undefined.

 console.log(3 + 4 + '5'); 

//   =75,  because it's the addition of 3+4 and you have on the string the number 5 that's you have the result of the addition to stick on value 5 it will be 75.






// exercise 5

typeof(15)
// Prediction: it's a number 
// Actual: number

console.log(typeof 15);

typeof(5.5)
// Prediction:it's a number
// Actual: number

typeof(NaN)
// Prediction: it's no number, that it will writing number
// Actual: number



typeof("hello")
// Prediction: it's value of the string because it's in "" 
// Actual:string


typeof(true)
// Prediction: it's a boolean
// Actual: boolean



typeof(1 != 2)
// Prediction: the ! thing it's mean that it's not ... here it's true that 1 don't = 2
// Actual: true



"hamburger" + "s"
// Prediction: it's additionate the hamburger with the s (stick the both string)
// Actual: hamburgers




"hamburgers" - "s"
// Prediction:it's not working because it's not number
// Actual: NaN

console.log("hamburgers" - "s");

"1" + "3"
// Prediction: 13, beacause it's the additionate of the string and don't of the number because there is  "".
// Actual: 13



"1" - "3"
// Prediction: 
// Actual: -2


console.log("1" - "3");


"johnny" + 5
// Prediction:
// Actual:

console.log("johnny" + 5);

"johnny" - 5
// Prediction:johnny5 because the string of value johnny with the number 5
// Actual: johnny5



99 * "hello"
// Prediction:NaN because it's multiplication betwwen number and word that it's not working
// Actual:NaN



1 != 1
// Prediction:false, because 1=1
// Actual: false





1 == "1"
// Prediction: true , 1=1
// Actual:true






1 === "1"
// Prediction: false, because miss you a thing, === it's for value and type;
// Actual: false


// exercise 6


5 + "34"
// Prediction: 534 because its 5 stick with the value 34
// Actual: 534




5 - "4"
// Prediction: 1 
// Actual: 1

console.log(5 - "4");

10 % 5
// Prediction: it's the modulus of the divisio,
// Actual: 0



5 % 10
// Prediction: 5, 5 don't divise with 10, that the rest is 5
// Actual: 5



"Java" + "Script"
// Prediction: JavaScript
// Actual: JavaScript




" " + " "
// Prediction: you don't have a values its nothing will come out.
// Actual: ....




" " + 0
// Prediction: space + 0 the only value 0
// Actual: space 0



true + true
// Prediction: true on jS it's 1 , it's 1+1=2
// Actual: 2


true + false
// Prediction: false it's 0 and true it's 1 that it true+false = 1
// Actual:1





false + true
// Prediction: false it's 0 and true it's 1 that it true+false = 1
// Actual:1



false - true
// Prediction: -true it's -1
// Actual:-1


!true
// Prediction: false, because ! its mean that it's not true
// Actual: false




3 - 4
// Prediction: -1, it's a soustraction between number
// Actual:-1



"Bob" - "bill"
// Prediction:NaN, it's not number
// Actual:NaN














