
let mousedown = false;



const listColor = ["blue", "red", "yellow", "green","grey", "pink", "black","purple","brown","cyan","lightgreen","indigo","white","lightskyblue","green","yellow","pink","orangered"];

for ( let i of listColor ) {

    const section1 = document.querySelector(".section1");
    const sectionNew = document.createElement("section");
    const div = document.createElement("div");
    div.setAttribute("id", i);
    sectionNew.style.backgroundColor = i;
    div.addEventListener("click", retrieveColor);
    sectionNew.appendChild(div);
    section1.appendChild(sectionNew);
   
   
}

 
function retrieveColor(evt) {
  evt.preventDefault();
  const color = evt.target.style.backgroundColor;   
}


const section2 = document.querySelector(".section2");

 for (let i = 0; i <= 1799; i++){
   
    const cell = document.createElement("div");
    cell.classList.add("cell");
  
    section2.appendChild(cell);
 }

 
    




 const button = document.querySelector("#btn");
 const cell = document.querySelector(".cell");

 button.addEventListener("click", function(){
    for (let i = 0; i <= 1799; i++){
        cell.style.backgroundColor = "white";}
    });




// let body = document.getElementsByTagName("body")[0];
// let mousedown = false;

// body.addEventListener("mousedown", function(){
//     mousedown = true;
// })

// body.addEventListener("mouseup", function(){
//     mousedown = false;
// })
