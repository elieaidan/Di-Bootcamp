// Using Javascript:
// Retrieve the div and console.log it
// Change the name “Pete” to “Richard”.
// Change each first name of the two <ul>'s to your name.
// Delete the <li> that contains the text node “Sarah”.



// // Récupérez le div et console.log it
// const firstDiv = document.getElementById("container");
// console.log(firstDiv);
// // Changez le nom "Pete" en "Richard".
// const firstUl = document.body.children[1];
// const secondLi = firstUl.lastElementChild;
// secondLi.textContent = "Richard";
// console.log(firstUl);
// // Remplacez chaque prénom des deux <ul>'s par votre nom.
// const allUL = document.getElementsByClassName("list");
// for(let ul of allUL){
//     ul.firstElementChild.textContent = "Elie";
// }
// console.log(allUL);
// // Supprimez le <li>qui contient le nœud de texte "Sarah".
// const secondUl = document.body.children[2]
// secondUl.children[1].remove();


// Exercice 2 : 


// document.body.firstElementChild.style.backgroundColor = "blue";
// document.body.firstElementChild.style.padding = "20px";
// const ul =  document.body.children[1];
// const list1 = ul.firstElementChild.style.display;
// const list2 = ul.lastElementChild.style.border = "thick solid #0000FF";
// document.body.style.fontSize = "100px";

// Exercise 3 :

// const division = document.body.firstElementChild;
// console.log(division);
// division.setAttribute(navBar, socialNetworkNavigation);

// Exercise 4 :




const allBooks = [] ;


const book1 = {
  title: "le roi lion ",
  author:" jerem sitbon",
  image: "jerem.jpg",
  alreadyRead: true
};


const book2 = {
  title: "la princesse ",
  author:" jerem brafman",
  image: "jerem.jpg",
  alreadyRead: false
};

allBooks.push(book1,book2);

console.log(allBooks);
console.log(${book1[title]});

// for ( let book of allBooks ){
  
 

//   const main = document.getElementById("listBooks");
//   const newP = document.createElement("p");
  
//   const content = document.createTextNode(`${book[`${title}`]}`);
//   newP.classList.add(content)
//   main.appendChild(newP);
// }
  








