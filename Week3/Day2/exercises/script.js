// Exercise 1 - basic addEventListener
// Create two buttons - id of "red", id of "blue"
// When we click on the red button -> Change the backgroundcolor of the page to red
// When we click on the blue button -> Change the backgroundcolor of the page to blue



// const btnfirst = document.querySelector("#red");
// const btnsecond = document.querySelector("#blue");

// btnfirst.addEventListener("click", background);
// btnsecond.addEventListener("click", background);

// function background (evt) {
    
//     document.body.style.backgroundColor = evt.target.value;
    
// }






// Exercise 2 - using the event object
// const colors = ["blue", "yellow", "green", "pink"];

// Add inside the HTML file a div of id "container" (do it directly in the HTML)
// Using a loop, add one button per color inside the div container (do it directly in the JS)
// Each button should have an "click" event listener that changes the background color of the document, to the color of the button (do it directly in the JS)const colors = ["blue", "yellow", "green", "pink"];


const colors = ["blue", "yellow", "green", "pink"];

function addButtons() {
  const divContainer = document.querySelector("#container");

  for ( let col of colors){
    const colordiv = document.createElement("button");
    colordiv.setAttribute("value", col);

    const content = document.createTextNode(col);
    colordiv.appendChild(content);
    divContainer.appendChild(colordiv);
    colordiv.addEventListener("click", background);
  }
}
addButtons();

function background (evt) {
    
     document.body.style.backgroundColor = evt.target.value;
  }




