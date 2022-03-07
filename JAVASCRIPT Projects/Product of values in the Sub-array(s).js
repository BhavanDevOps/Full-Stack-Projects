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
  const nestedArray = JSON.parse(readLine());

   const resultArray = nestedArray.map(arr => {
        if ( arr.some(item => item % 2 === 0) ) {
            return arr.reduce( (acc, current) => acc * current )
        } else {
            return 0
        }
    });
    console.log(resultArray);

}
