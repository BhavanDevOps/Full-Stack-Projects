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

function ArithmeticOperations(firstNumber, secondNumber) {
  this.firstNumber = firstNumber;
  this.secondNumber = secondNumber;
}

function main() {
  const firstNumber = JSON.parse(readLine());
  const secondNumber = JSON.parse(readLine());
  
  const operation1 = new ArithmeticOperations(firstNumber, secondNumber);
  
  ArithmeticOperations.prototype.sumOfNumbers=function(){
      const sum=this.firstNumber+this.secondNumber;
      return sum;
  };
  
    ArithmeticOperations.prototype.productOfNumbers=function(){
      const product=this.firstNumber*this.secondNumber;
      return product;
  };
  
    ArithmeticOperations.prototype.differenceOfNumbers=function(){
      const difference=this.firstNumber-this.secondNumber;
      return difference;
  };

  console.log(operation1.sumOfNumbers());
  console.log(operation1.productOfNumbers());
  console.log(operation1.differenceOfNumbers());
}