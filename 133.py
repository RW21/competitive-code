from collections import deque
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        copy_node = Node(node.val, [])

        hash_ = dict()
        queue = deque()

        queue.append(node)
        hash_[node] = copy_node

        while queue:
            node = queue.popleft()
            
            for n in node.neighbors:
                if n not in hash_:
                    queue.append(n)
                    hash_[n] = Node(n.val, [])
                hash_[node].neighbors.append(hash_[n])
                
        return copy_node


