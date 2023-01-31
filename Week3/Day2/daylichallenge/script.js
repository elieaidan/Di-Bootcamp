// Dans l'exercice d'aujourd'hui, nous allons créer un jeu Mad Libs.
// Si vous n'avez jamais joué à ce jeu, une lib folle est un jeu où vous remplissez un tas d'entrées vides avec différents types de mots (c'est-à-dire : nom, adjectif, verbe), puis une histoire est générée en fonction des mots que vous avez choisis , et parfois l'histoire est étonnamment drôle.

// Dans cet exercice, vous travaillez avec le code HTML présenté ci-dessous.

// Suivez ces étapes:

// Obtenez la valeur de chacune des entrées dans le fichier HTML lorsque le formulaire est soumis. Rappelez-vous le event.preventDefault()
// Assurez-vous que les valeurs ne sont pas vides
// Écrivez une histoire qui utilise chacune des valeurs.
// Assurez-vous de vérifier la console pour les erreurs lors de la lecture du jeu.


const formDC = document.querySelector("#libform");

formDC.addEventListener("submit", text);

sphereform.addEventListener("submit", text);

function text (evt) {

    evt.preventDefault();
    const allinputs = formDC.querySelectorAll("input");
    const allValues= [];
    for(let input of allinputs){
        allValues.push(input.value)
    }
    console.log(allValues);

    const sentence = `bla ${allValues[0]} bla  ${allValues[1]} bla ${allValues[2]} bla ${allValues[3]}`;
    console.log(sentence);


}


    
