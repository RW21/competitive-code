"""
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        checked = set()
        
        left = 0
        right = 0
        count = 0
        length = len(s)

        while (left < length and right < length):
            if s[left] not in checked:
                checked.add(s[left])
                left += 1
                count = max(count, left - right)
            else:
                checked.discard(s[right])
                right += 1

        return count
