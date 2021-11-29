var sentences = [
  "Merry Christmas!",
  "Have fun!",
  "Season's Greetings!",
  "I wonder if people will recognize this is interactive.",
  "Made any Mince Py's yet?",
  "I should be doing something else..",
  "This is fun!",
  "I'm terrible at puns. It's really quit pythetic",
  "I certainly hope you havn't spent more than a few minutes on this!",
  "Tis the season to be coding",
  "Have a nice cup of Java",
  "Are you still on this?",
  "Wonder if you'll ever see this sentence!",
  ":)",
  "Don't forget to submit your entries!",
  "Why am I even bothering to be punny?",
];

function newSentence() {
  var sentence = Math.floor(Math.random() * sentences.length);
  document.querySelector(".christmas").innerText = sentences[sentence];
}

// Thanks to @Bookie0 for this code inspiration! - Check out his Portfolio! https://bookie0.repl.co/
