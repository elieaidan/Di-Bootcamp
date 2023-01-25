// 1. Create a structured HTML file linked to a JS file

// 2. Write a Javascript function that takes a parameter: myAge

// 3. In the function, console.log the age of my mum and my dad. My mum is twice my age, and my dad is 1.2 the age of my mum.

// 4. Call the function.

// function age (myAge){
//   let  mumage = 2*myAge
//   let  dadage = 1.2*mumage
//   console.log(mumage);
//   console.log(dadage);
// }

// age(20);


// Exercise 1
// You are the manager of the chocolate factory, in order to make your clients happy you will send them a gift depending on their quantity of chocolate box they ordered.

// Create a function named checkQuantityOrder, that takes one parameter, the quantity the user ordered.

// If the client ordered more between 5 and 10 boxes (included) console.log "Dear client, you won a bouquet of flowers"
// If the client ordered more between 10 and 20 boxes (included) console.log "Dear client, you won a bottle of wine"
// If the client ordered more than 20 boxes (included) console.log "Dear client, you won a trip to Paris"
// Call the function a few times,

// checkQuantityOrder(8);
// checkQuantityOrder(15);
// checkQuantityOrder(30);

// BONUS : add a parameter to the function, the name of the client. If you don't know the name of the client, call him/her "client"

// If the client ordered more between 5 and 10 boxes (included) console.log "Dear <name_client>, you won a bouquet of flowers"
// If the client ordered more between 10 and 20 boxes (included) console.log "Dear <name_client>, you won a bottle of wine"
// If the client ordered more than 20 boxes (included) console.log "Dear <name_client>, you won a trip to Paris"
// Call the function a few times,

// checkQuantityOrder(8, "John");
// checkQuantityOrder(15);
// checkQuantityOrder(30, "David");

const name = prompt("What is your name?");
const name1 = name.toLowerCase()

function checkQuantityOrder (quantity){
    if(quantity<=10 && quantity>5) {
        console.log(`Dear ${name1}, you won a bouquet of flowers`);
    } else if (quantity<20 && quantity>10){
        console.log(`Dear ${name1}, you won a bottle of win`);
    } else if (quantity>=20){
        console.log(`Dear ${name1}, you won a trip to Paris`);
    }


}

checkQuantityOrder(8);
checkQuantityOrder(15);
checkQuantityOrder(30);
