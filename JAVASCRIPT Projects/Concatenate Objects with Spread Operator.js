"use strict";

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", (inputStdin) => {
  inputString += inputStdin;
});

process.stdin.on("end", (_) => {
  inputString = inputString
    .trim()
    .split("\n")
    .map((str) => str.trim());

  main();
});

function readLine() {
  return inputString[currentLine++];
}

function main() {
  let model = JSON.parse(readLine().replace(/'/g, '"'));
  let engine = JSON.parse(readLine().replace(/'/g, '"'));
  let carDetails = {
  };
  carDetails={...model,...engine};
/* Please do not modify anything below this line */  
  console.log(`${carDetails.model} is powered with ${carDetails.engineCapacity}cc engine.`);
}
