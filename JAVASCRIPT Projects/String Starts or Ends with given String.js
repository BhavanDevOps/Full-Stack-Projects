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
  const stringsArray = JSON.parse(readLine().replace(/'/g, '"'));
  const startString = readLine();
  const endString = readLine();

  function filterString(stringsArray, startString, endString) {
    return stringsArray.filter( item => item.startsWith(startString) || item.endsWith(endString) )
}
const stringsArray1 = stringsArray;
const startString1 = startString;
const endString1 = endString;
const filterArray1 = filterString(stringsArray1, startString1, endString1);
console.log(filterArray1);
}
