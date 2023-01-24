
// DailyChallenge


const sentence = "The movie is not that bad, I like it";

const wordNot = sentence.indexOf("not");

const wordBad = sentence.indexOf("bad");

console.log(wordNot);

console.log(wordBad);



 if (wordNot < wordBad && wordNot!==-1 && wordBad!==-1)  {

    console.log(`The movie is good, I like it`);


 } else {


    console.log(`The movie is not that bad, I like it`);


 }




