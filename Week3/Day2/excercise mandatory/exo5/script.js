const p1 = document.getElementById("p1");
const h1 = document.body.firstElementChild;
const btn1 = document.getElementById("btn");
const p2 = document.getElementById("p2");


h1.addEventListener("click", coucou());

p1.addEventListener("mouseover", over());

btn1.addEventListener("mouseout", wesh());

// p2.addEventListener("scroll", myScript);


function coucou (){
    document.body.style.backgroundColor= "blue";
    
}


function over() {
    p1.style.fontSize = "x-large";
    
}


function wesh() {
    btn1.style.borderImage = "url(border.png) 30 30 round";
    
}





