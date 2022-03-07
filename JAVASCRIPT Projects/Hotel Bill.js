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
  const dayCharge = JSON.parse(readLine());
  const days = parseInt(readLine());
  let bill,discount;
  
  bill= dayCharge * days;
  let discountedBill;
  if(days >2 && days <=5){
      discount = 5;
      discountedBill = bill - (bill * discount)/100;
  }
   if(days >5){     //No need to provide =5 days
   discount=15;
   discountedBill=bill-(bill *discount)/100;
} if(days < 2) {        //Calculate discountedBill when days are less than 2
    discountedBill = dayCharge * days;
}
 console.log(discountedBill);

 

  /* Write your code here */
}