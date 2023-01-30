

const solarsystem = [{
    name : "mercure",
    moon : 1,
},
{
    name : "earth",
    moon : 3,
},
{
    name : "jupiter",
    moon : 7,
},

];









 
function addplanets () {
    

   const section = document.querySelector(".listPlanets");
         for ( let planet of solarsystem){
           const planetDiv = document.createElement("div");
           const content = document.createTextNode(planet["planetName"]);
           planetDiv.classList.add("planet", planet["planetName"]);
         planetDiv.appendChild(content);


     }}
addplanets(); 
