import itertools


class Solution:
    def backspaceCompare(self, S, T):
        def process(string):
            skip = 0
            for character in reversed(string):
                if character == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield character

        return all(i == j for i, j in itertools.zip_longest(process(S), process(T)))
