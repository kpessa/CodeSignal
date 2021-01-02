"""
You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

Example

For inputArray = [1, 1, 1], the output should be
arrayChange(inputArray) = 3.
"""

# %%

inputArray = [-1000, 0, -2, 0]


def arrayChange(inputArray):
    moves = 0
    previous = inputArray.pop(0)
    for current in inputArray:
        if current > previous:
            previous = current
        else:
            moves += previous - current + 1
            previous = previous + 1
    return moves


arrayChange(inputArray)
