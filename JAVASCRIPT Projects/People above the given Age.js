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
  const ageLimit = parseInt(readLine());
  const peopleAge = JSON.parse(readLine());

  function checkEachArrayWithAgeLimit(eachArray){
      return eachArray.every((age)=>age>ageLimit);
  }
  const result=peopleAge.map((each)=>checkEachArrayWithAgeLimit(each));
  console.log(result);
}
