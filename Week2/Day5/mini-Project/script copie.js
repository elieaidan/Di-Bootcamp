// Exercise 1


// Part 1


// Dans le fichier JS, créez une fonction appelée playTheGame() qui ne prend aucun paramètre.
// Dans la fonction, commencez par demander à l'utilisateur s'il souhaite jouer au jeu 
// (Astuce : utilisez la fonction intégrée confirm()).

// Si la réponse est fausse, alertez « Pas de problème, au revoir ».

// Si sa réponse est vraie, suivez ces étapes :
// Demandez à l'utilisateur d'entrer un nombre entre 0 et 10
//  (Astuce : utilisez la fonction intégrée prompt()). Vous devez ensuite vérifier la validité du numéro d'utilisateur :

// Si l'utilisateur n'a pas saisi de numéro (c'est-à-dire s'il a saisi un autre type de données),
//  l'alerte "Désolé, pas un numéro, au revoir".
// Si l'utilisateur n'a pas saisi de chiffre entre 0 et 10,
//  l'alerte "Désolé, ce n'est pas un bon chiffre, au revoir".
// Sinon (c'est-à-dire qu'il a entré un nombre entre 0 et 10), 
// créez une variable nommée computerNumber où la valeur est un nombre aléatoire entre 0 et 10
//  (Astuce : utilisez la fonction intégrée Math.random()). Assurez-vous que le nombre est arrondi.





function playTheGame() {
  let number;
  let computerNumber;
  let result;
    function confirm (){
     let question = prompt("Would like to play the game?");
     let answer = question.toLowerCase();
        if ( answer === yes ){
          number = prompt("Chose a number betwwen 0 and 10");
          let rep = Number(number);

            if (rep === NaN){

            return "Désolé, pas un numéro, au revoir";

          } else if (rep>10  || rep <0) {

           return "Désolé, ce n'est pas un bon chiffre, au revoir";

          } else {
            computerNumber = Math.random() * 10;
            result = Math.round(computerNumber);
            
            return result;
          }



        }else {
        console.log(`No problem, GoodBye.`);
        return "No problem, GoodBye.";
        
        }
          
    }
}
playTheGame();




// Second Part



// En dehors de la fonction playTheGame(),
// créez une nouvelle fonction nommée
//  compareNumbers(userNumber,computerNumber) qui prend 2 paramètres : userNumber et computerNumber

// Le but de cette fonction est de vérifier si le userNumber est le même que le computerNumber :
// Si userNumber est égal à computerNumber, alertez "WINNER" et arrêtez le jeu.

// Si userNumber est plus grand que computerNumber,
// alerte "Votre numéro est plus grand que celui de l'ordinateur, devinez à nouveau"
// (Astuce : utilisez la fonction intégrée prompt() pour demander à l'utilisateur un nouveau numéro).

// Si userNumber est inférieur à computerNumber,
// alerte "Votre numéro est plus petit que celui de l'ordinateur, devinez à nouveau"
// (Astuce : utilisez la fonction intégrée prompt() pour demander à l'utilisateur un nouveau numéro).

// Si l'utilisateur a deviné plus de 3 fois, alertez "hors de chances" et quittez la fonction.


function compareNumbers(userNumber,computerNumber){
    if ( userNumber === playTheGame()){
      alert("WINNER");
      return alert
    }else if (userNumber > playTheGame()){
       prompt("Votre numéro est plus grand que celui de l'ordinateur, devinez à nouveau");
       return prompt
      
    }else if (userNumber < playTheGame()){
      prompt("Votre numéro est plus petit que celui de l'ordinateur, devinez à nouveau");
      return prompt
    }

    
}