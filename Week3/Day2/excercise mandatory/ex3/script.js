

let allBoldItems;


function  getBold_items() {
  allBoldItems = document.querySelectorAll("p strong");
  
}

getBold_items();

console.log(allBoldItems);

// function highlight(){
//     allBoldItems.style.color = "blue";
   
// }

// highlight();

function highlight() {

  for ( let boldd of allBoldItems){
    const git = boldd.style.color = "blue";
    console.log(git);
  }

}

 highlight(); 
 
 function return_normal() {

    for ( let ret of allBoldItems){
      const git2 = ret.style.color = "black";
      console.log(git2);
    }
  
  }


return_normal();


document.querySelector("p").addEventListener("mouseover", highlight);
document.querySelector("p").addEventListener("mouseout", return_normal);