"""
You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.

Example

For inputArray = [5, 3, 6, 7, 9], the output should be
avoidObstacles(inputArray) = 4.

Check out the image below for better understanding:
"""

# %%

inputArray = [49, 607, 611, 815, 378, 200, 731, 252, 295, 175, 676, 244, 713, 701, 208, 662, 672, 896, 534, 476, 745, 231, 497, 398, 913, 145, 211, 886, 693, 384, 843, 937, 76, 407, 733, 647, 96, 226, 117, 359, 525, 15, 298, 341, 503, 823, 952, 483, 457,
              223, 436, 89, 427, 91, 584, 902, 989, 968, 498, 983, 749, 742, 608, 967, 422, 945, 763, 355, 600, 702, 666, 195, 333, 157, 228, 828, 874, 948, 565, 625, 859, 394, 652, 804, 853, 113, 347, 772, 10, 855, 446, 156, 19, 306, 555, 663, 177, 917, 829, 12]

[x / 55 for x in inputArray]
# %%


def avoidObstacles(inputArray):
    for i in range(2, 1000):
        result = True
        for item in inputArray:
            if item % i == 0:
                result = False
        if result:
            return i


print(avoidObstacles(inputArray))
