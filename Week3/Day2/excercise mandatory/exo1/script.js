
// exercice 1

const article = document.body.firstElementChild;
const firsth1 = article.firstElementChild;

console.log(firsth1);




article.removeChild(lastp);

console.log(lastp);


const theh2 = article.querySelector("#chocolate");

theh2.addEventListener("click", background);

function background (){
    theh2.style.backgroundColor = "red";
}

const theh3 = article.querySelector("#history");

theh3.addEventListener("click", hidden);

function hidden (){
    theh3.style.display = "none";;
 }

 const btn = document.querySelector("#btn1");

 btn.addEventListener("click", bold);

function bold() {
    
    document.body.style.fontWeight = "bold";
}





