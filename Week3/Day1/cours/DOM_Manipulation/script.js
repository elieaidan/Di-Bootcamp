function changeParagraph () {
    const title = document.body.firstElementChild;
    const division = title.nextElementSibling;
    const paragraph =  division.firstElementChild;
    console.log(paragraph);
    paragraph.textContent = "Great!!"
}

changeParagraph()
// title.textContent = "Good Morning";

//access the second div on the page
const secondDiv = document.body.children[2];
//access the first child of the div
const paragraphOfSecondDiv = secondDiv.firstElementChild;
//change the text content of the paragraph inside the second div
paragraphOfSecondDiv.textContent = "How are you";

// Change the style
// change the background color of the H1
document.body.firstElementChild.style.backgroundColor = "yellow";
document.body.style.fontSize = "10px";

