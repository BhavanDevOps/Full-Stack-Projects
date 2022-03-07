"use strict";

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", (inputStdin) => {
  inputString += inputStdin;
});

process.stdin.on("end", (_) => {
  inputString = inputString.trim().split("\n").map((str) => str.trim());
  main();
});

function readLine() {
  return inputString[currentLine++];
}

/* Please do not modify anything above this line */

function main() {
  const inputString = readLine();
  const vowels = ['A', 'E', 'I', 'O', 'U'];
  
  const upperString=inputString.toUpperCase();
  if (upperString.endsWith('E') || upperString.endsWith('U') || upperString.endsWith('I') || upperString.endsWith('O') || upperString.endsWith('A')) {
    console.log('true');
} else {
    console.log('false');
}
}