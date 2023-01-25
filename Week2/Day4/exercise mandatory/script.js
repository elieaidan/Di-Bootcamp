// Exercise 1

// Partie I

// function infoAboutMe(){
//     const name = "Elie" ;
//     const age = 20;
//     const hobbies = ["learn torah", " to code", "football"];
//     console.log(`My name is ${name} i am ${age} years old and my hobbies is ${hobbies}.`);
//  }

// infoAboutMe();

// Partie II

// function infoAboutPerson(personName, personAge, personFavoriteColor){
//       console.log(`You name is ${personName}, you are ${personAge} years old, your favorite color is ${personFavoriteColor}`);

// }

// infoAboutPerson("David", 45, "blue");
// infoAboutPerson("Josh", 12, "yellow");





// Exercise 2


//  function calculateTip(){
//    const amountbill = prompt('What is the price for the amount bill?');
//    const number = Number(amountbill);
//    let tip;
//    if ( number < 50){
//     tip = 0.2 * number;
//    }
//    else if ( number >= 50 && number <= 200){
//      tip = 0.15* number;
//    }
//    else if ( number > 200){
//      tip = 0.1* number; 
//    }

//    console.log(number + tip );
   
//  }


//  calculateTip();


//  Exercise 3

// function isDivisible() {
//   let sum = 0;
//   for(i = 0 ; i <= 500 ; i ++){
//     if(i % 23 === 0){
//     console.log(`Outcome : ${i}`);
//     sum += i;
//    }
// }
//   console.log(`Sum : ${sum}`);

// }

// isDivisible();




// Exercice 4


// const stock = { 
//     "banana": 6, 
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry":1
// }  

// const prices = {    
//     "banana": 4, 
//     "apple": 2, 
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry":10
// } 

//  const shoppingList = ["banana", "orange", "apple", "hugjbvh"];




// function myBill() {
//    let total = 0;
   
//     for(let i= 0 ; i < shoppingList.length ; i ++ ){
//         let item = shoppingList[i];
//         if (item in stock){
//             if (stock[item] > 0){
//                 total += prices[item];
               
//               }else{
//                 console.log(`${item} is out of stock`);
//                 }  
//          }else{
//            console.log(`${item} is not a valid item`);
//           }

//     }
//     console.log(total);
// }

// myBill()

// Exercice 5 

// function changeEnough(itemPrice, amountOfChange){
     
//       if (changeEnough >= itemPrice){
//         return True
//     }else if (changeEnough < itemPrice){
//         return False
//     }
    
// }

// changeEnough = (10, [, 20, 5, 0]);
// // for (let i = 0; i < array.length; i += 1) {
// //     // take every item in the array and add it to sum variable
// //     sum += array[i]


// Exercise 6

function hotelCost (){
    let numberofnight = prompt('How night would you want to stay in the hotel?');
    // let numberofnights = Number.numberofnight;
    if (numberofnight === !Number){
       prompt('How night would you want to stay in the hotel?')
        return  
    }
}


hotelCost();