"""
Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

Example

For s = "abacabad", the output should be
firstNotRepeatingCharacter(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

For s = "abacabaabacaba", the output should be
firstNotRepeatingCharacter(s) = '_'.

There are no characters in this string that do not repeat.
"""

# %%

s = "abacabaabacaba"


def firstNotRepeatingCharacter(s):
    from collections import OrderedDict, Counter

    class OrderedCounter(Counter, OrderedDict):
        pass
    counter = OrderedCounter(s)
    if all([x >= 2 for x in counter.values()]):
        return '_'
    else:
        for i in range(0, len(counter.keys())):
            if counter.values()[i] == 1:
                return counter.keys()[i]


print(firstNotRepeatingCharacter(s))

# %%
