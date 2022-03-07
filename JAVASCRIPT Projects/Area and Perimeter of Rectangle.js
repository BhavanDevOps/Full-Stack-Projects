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

function Rectangle(length, breadth) {
  this.l=length;
  this.b=breadth;
  this.getArea=function(){
      return this.l*this.b;
  };
  this.getPerimeter=function(){
      return 2*(this.l+this.b);
  };
}

/* Please do not modify anything below this line */

function main() {
  const l = JSON.parse(readLine());
  const b = JSON.parse(readLine());
  
  const rectangle = new Rectangle(l, b);
  
  console.log(rectangle.getArea());
  console.log(rectangle.getPerimeter());
}