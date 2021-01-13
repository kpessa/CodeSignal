/*
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
adjacentElementsProduct(inputArray) = 21.

7 and 3 produce the largest product.
*/

var inputArray = [3, 6, -2, -5, 7, 3];

var output = console.log(output);

console.log(...inputArray.slice(1));

function adjacentElementsProduct(inputArray) {
  var max = inputArray[0] * inputArray[1];
  if (inputArray.length > 2) {
    for (var i = 2; i < inputArray.length; i++) {
      if (inputArray[i] * inputArray[i - 1] > max) {
        max = inputArray[i] * inputArray[i - 1];
      }
    }
  }
  return max;
}

// Better solution using spread syntax, Math.max, slice(1) taking the next value.
var inputArray = [3, 6, -2, -5, 7, 3];

function adjacentElementsProduct(arr) {
  return Math.max(...arr.slice(1).map((x, i) => x * arr[i]));
}

console.log(adjacentElementsProduct(inputArray));
