"""
Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

Example

For inputArray = [2, 4, 1, 0], the output should be
arrayMaximalAdjacentDifference(inputArray) = 3.
"""

# %%

inputArray = [2, 4, 1, 0]


def arrayMaximalAdjacentDifference(inputArray):
    max = 0
    for i in range(1, len(inputArray)):
        difference = abs(inputArray[i-1]-inputArray[i])
        if difference > max:
            max = difference

    return max


print(arrayMaximalAdjacentDifference(inputArray))
