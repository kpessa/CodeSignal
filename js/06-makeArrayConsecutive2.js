/*
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

Example

For statues = [6, 2, 3, 8], the output should be
makeArrayConsecutive2(statues) = 3.

Ratiorg needs statues of sizes 4, 5 and 7.
*/

var statues = [6, 2, 3, 8];

function makeArrayConsecutive2(statues) {
  statues.sort(); // [6, 2, 3, 8]

  var dif = Math.max(...statues) - Math.min(...statues); // 6
  return dif - statues.length + 1; // 6 - 4 + 1 = 2
}

console.log(makeArrayConsecutive2(statues));

console.assert(makeArrayConsecutive2([6, 2, 3, 8]) == 3);
