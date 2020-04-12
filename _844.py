class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        S = list(S)
        T = list(T)

        for i in range(len(max(S, T))):
           if i >