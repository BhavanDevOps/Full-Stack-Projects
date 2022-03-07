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

function logFamily(father,mother,...children){
    let formatedChildren=children.join();
    console.log(`${father} ${mother}`);
    console.log(formatedChildren);
}
function main() {
  let familyArray = JSON.parse(readLine().replace(/'/g, '"'));

  logFamily(...familyArray);
}
