from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)

        for string in strs:
            characters = [0] * 26
            for char in string:
                characters[ord(char) - ord('a')] += 1
            results[str(characters)].append(string)

        return list(results.values())
