class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            if c in mapping:
                if len(stack) == 0:
                    return False
                if stack.pop() != mapping[c]:
                    return False
            else:
                stack.append(c)

        if len(stack) != 0:
            return False
        return True


print(Solution().isValid(']'))
