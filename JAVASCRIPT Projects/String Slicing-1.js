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
  let inputString = readLine();
  const subString = readLine();
  if(inputString.includes(subString)) {
    let index=inputString.indexOf(subString);
    let r=inputString.slice(index);
    console.log(r);
} else {
    console.log(inputString);
}
  //let index=inputString.indexOf(subString);
//  let r=inputString.slice(index);
 // console.log(r);
}
