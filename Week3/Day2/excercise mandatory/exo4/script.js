const sphereform = document.querySelector("#MyForm");

// document.forms[0];
// document.forms.MyForm;

sphereform.addEventListener("submit", calculatevolume);

function calculatevolume(evt) {
    
   evt.preventDefault();
   const input = evt.target.radius.value;
   const volume = input**3;
   const inputVolume = evt.target.volume;
   inputVolume.value = volume;
   
}

