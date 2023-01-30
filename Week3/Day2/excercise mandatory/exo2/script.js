

const form = document.forms;
console.log(form);


// const input1 = document.querySelector("#fname");
// console.log(input1);

// const input2 = document.querySelector("#lname");
// console.log(input2);



const input1 = document.getElementsByName("fname")[0];
console.log(input1);

const input2 = document.getElementsByName("lname")[0];
console.log(input2);

const submit = document.querySelector("#submit");
submit.addEventListener("click", function(evt) {
    evt.preventDefault(); 
    //it stops the default action of the submission
    //the page will not refresh
    const fname = input1.value;
    const lname = input2.value;

    if (!fname && !lname){
        return
    }
})

// function retrieveValue (evt) {
//     evt.preventDefault(); 
//     //it stops the default action of the submission
//     //the page will not refresh
//     const fname = fnameInput.value;
//     const lname = lnameInput.value;
    
//     // const para =  document.createElement("p");
//     // const text = document.createTextNode(`the user types ${fname} ${lname}`);
//     // para.appendChild(text);
//     // document.body.appendChild(para)
    
// }


