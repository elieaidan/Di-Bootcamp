

const input = document.querySelector("#text");

input.addEventListener("keypress", function(event) {
  const charCode = event.charCode;
  // Check if the pressed character is a letter
  if (!(charCode >= 65 && charCode <= 90) && !(charCode >= 97 && charCode <= 122)) {
    event.preventDefault(); // prevent the character from being added to the input
  }
});
