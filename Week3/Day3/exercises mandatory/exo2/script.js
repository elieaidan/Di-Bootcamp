

let btn = document.querySelector("#btn");
let carre = document.querySelector("#animate");

// click event
btn.addEventListener("click", carrerouge );

function carrerouge () {
      let start = Date.now();

      let timer = setInterval(function() {
        let timePassed = Date.now() - start;
        console.log(timePassed)
        carre.style.left = timePassed / 5.9 + 'px';
        if (timePassed > 2000) {
          clearInterval(timer);
        }
      }, 20);
    }