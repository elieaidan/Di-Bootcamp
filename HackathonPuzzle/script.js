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
            img.src = `./images/${randomNum}.jpeg`;
            img.setAttribute("id", randomNum);
            secondpart.appendChild(img);
            arrnum.splice(arrnum.indexOf(randomNum), 1)
            img.addEventListener("dragstart",startDragging)
            // img
        }
    }
}
addImages();

function divs(){
    for (let i = 1; i <=16; i++) {
        let div =document.createElement("div")
        // let tile = document.createElement("img");
        // div.appendChild(tile)
        div.dataset.tag=[i]
        document.getElementById("main").append(div);
    }
}
divs()

function startDragging(evt){
    evt.target.classList.add("startDrag");
    evt.dataTransfer.setData("text/plain", evt.target.id);
    //use the dataTransfer object, to set the data that we want to drop in the future
    console.log(evt.target.id); //box I drag
}

function retrieveZonesAndAddEvents () {
    const allZones = document.querySelectorAll("#main div");
    // console.log(allZones);
    for (let zone of allZones) {
        zone.addEventListener("dragover", overTarget);
        zone.addEventListener("drop", dropOnTarget);
    }
}
retrieveZonesAndAddEvents()

function overTarget (evt) {
    evt.preventDefault(); //necessary
    evt.target.classList.add("overDrop");
}

function dropOnTarget (evt) {
    evt.preventDefault();  //necessary
    evt.target.classList.add("droppedTarget");
    const n1 = evt.dataTransfer.getData("text/plain")
    // console.log(n1);
    const elem = document.getElementById(n1)
    evt.target.appendChild(elem)
}
// function end(evt){
//     for (let i = 1; i <=16; i++) {
//         const n2=document.getElementById(i)
//         const n3=document.querySelector("div[data-tag]").getAttribute("data-tag")[i]
//         console.log(n3);
//         console.log(n2);
//         if(n2 == n3){
//             alert('You win')
//         }
//     }
// }
// end()
