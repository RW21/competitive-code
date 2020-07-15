import heapq


class Solution:
    def lastStoneWeight(self, stones) -> int:
        q = [-stone for stone in stones]
        heapq.heapify(q)
        while (len(q)) > 1:
            heapq.heappush(q, heapq.heappop(q) - heapq.heappop(q))
        return -q[0]


print(Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]))
