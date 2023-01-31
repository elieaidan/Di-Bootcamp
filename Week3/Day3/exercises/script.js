
// exercise 1


setTimeout(sayHi, 1000);

function sayHi() {
    const containerSection =  document.querySelector("#container")
    const newParagraph = document.createElement("p");
    const content = document.createTextNode("The sales end in 10min !");
    newParagraph.appendChild(content);
    containerSection.appendChild(newParagraph);
  }
  

// exercise 2


 
  