const secondpart = document.querySelector("#secondpart");
function addImages(){
    const arrnum = [];
    for (let i = 1; i <= 16; i++) {
        arrnum.push(i)
    }

    while (arrnum.length !== 0) {
        let randomNum = Math.floor(Math.random() * 16) + 1;
        if(arrnum.includes(randomNum) == true) {
            const img = document.createElement("img");
            img.src = `imagesp${randomNum}.jpeg`;
            img.setAttribute("class", "flex-item");
            img.setAttribute("draggable", true);
            secondpart.appendChild(img); 
            arrnum.splice(arrnum.indexOf(randomNum), 1);
            img.addEventListener("dragstart", startDragging);
            
            
        }
    }
}
addImages();


function startDragging(evt){
  evt.target.classList.add("startDrag");
  evt.dataTransfer.setData("text/plain", evt.target.id);

}





const firstpart = document.querySelector("#main");
console.log(firstpart);


 function addDiv(){

    for ( let i = 1; i <=16 ; i++){

        const divfirstpart = document.createElement("div");
        divfirstpart.classList.add("border");
        divfirstpart.setAttribute("class", "grid-item");
        firstpart.appendChild(div);
         for (let zone of div) {
          zone.addEventListener("dragover", overTarget);
          zone.addEventListener("drop", dropOnTarget);
        }

    }
      
}
addDiv();


function overTarget (evt) {
  evt.preventDefault();
  evt.target.classList.add("overDrop");
}

function dropOnTarget (evt) {
  evt.preventDefault();  
  evt.target.classList.add("droppedTarget");
  const data = evt.dataTransfer.getData("text/plain");
  const elem = document.getElementById(data);
  evt.target.appendChild(elem);
  console.log(evt);
}






