

const todrive = 18 ;
const question = prompt("How old are you?");

if(question >= todrive){
   console.log("Powering On. Enjoy the ride!"); 

} else if(question === todrive){
    console.log("Congratulations on your first year of driving. Enjoy the ride!"); 


}
else if (question < todrive) {

    console.log("Sorry, you are too young to drive this car."); 

}