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
  let numbersArray = JSON.parse(readLine());

/* Please do not modify anything above this line */
    let [firstNumber,secondNumber,...rest]=numbersArray;
    let sum=0;
    for (let eachNumber of rest){
        sum+=eachNumber;
    }
    console.log(sum);
  /*
   * Write your code here and log the output.
   */
}
