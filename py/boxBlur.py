"""
Last night you partied a little too hard. Now there's a black and white photo of you that's about to go viral! You can't let this ruin your reputation, so you want to apply the box blur algorithm to the photo to hide its content.

The pixels in the input image are represented as integers. The algorithm distorts the input image in the following way: Every pixel x in the output image has a value equal to the average value of the pixel values from the 3 × 3 square that has its center at x, including x itself. All the pixels on the border of x are then removed.

Return the blurred image as an integer, with the fractions rounded down.

For

image = [[1, 1, 1], 
         [1, 7, 1], 
         [1, 1, 1]]
the output should be boxBlur(image) = [[1]]
"""

# %%

image = [[36, 0, 18, 9, 9, 45, 27],
         [27, 0, 54, 9, 0, 63, 90],
         [81, 63, 72, 45, 18, 27, 0],
         [0, 0, 9, 81, 27, 18, 45],
         [45, 45, 27, 27, 90, 81, 72],
         [45, 18, 9, 0, 9, 18, 45],
         [27, 81, 36, 63, 63, 72, 81]]


def boxBlur(image):
    return [[int(sum(sum(x[i:i+3]) for x in image[j:j+3])/9) for i in range(len(image[0])-2)] for j in range(len(image)-2)]


print(boxBlur(image))

# %%
result = [[0]]

result[0][0] += sum(i[0:])

print(result)

# %%


def boxBlur(i):
    for r in range(1, len(i)-2):
        for c in range(1, len(i)-2):
            result[r-1][c-1] += i[r-1][c-1] + i[r-1][c] + i[r-1][c+1]
            result[r-1][c-1] += i[r][c-1] + i[r][c] + i[r][c+1]
            result[r-1][c-1] += i[r+1][c-1] + i[r+1][c] + i[r+1][c+1]

    return result


print(boxBlur(i))

# %%
i = [[1, 1, 1],
     [1, 7, 1],
     [1, 1, 1]]
print(range(1, len(i)-2))

# %%
