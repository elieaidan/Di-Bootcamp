// Part I

// setTimeout(sayHello, 2000);
// function sayHello() {
//     alert('Hello World');
    
// }

// Partie II


// const container = document.querySelector("#container");

// setTimeout(sayHello2, 2000);
// function sayHello2() {
//    const newParagraph = document.createElement("p");
//    const content = document.createTextNode("Hello World");
//    newParagraph.appendChild(content);
//    container.appendChild(newParagraph);  
// }



// Partie III

const dInterval = setInterval(changeNumber, 2000);


let counter = 5;

function changeNumber() {
  
    if(counter >= 0) {
        const newParagraph = document.createElement("p");
        const content = document.createTextNode("Hello World");
        newParagraph.appendChild(content);
        container.appendChild(newParagraph);
        counter --;
       
    } else { 
        clearInterval(dInterval);
    }
}

