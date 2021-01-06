"""
Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
palindromeRearranging(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.
"""

# %%

inputString = "abbcabb"


def palindromeRearranging(inputString):
    from collections import Counter
    cnt = Counter(inputString)

    remainder = 0
    for value in cnt.values():
        remainder += value % 2

    if remainder in (0, 1):
        return True
    else:
        return False


print(palindromeRearranging(inputString))
