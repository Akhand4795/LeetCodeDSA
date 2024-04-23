class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        # Construct the adjacency list
        graph = {i: set() for i in range(n)}
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        # Initialize the queue with leaf nodes
        leaves = deque(i for i in range(n) if len(graph[i]) == 1)
        
        # Keep removing leaves until only the MHTs remain
        while n > 2:
            num_leaves = len(leaves)
            n -= num_leaves
            
            # Remove the current level of leaves
            for _ in range(num_leaves):
                leaf = leaves.popleft()
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                
                # Add the neighbor to the queue if it becomes a leaf
                if len(graph[neighbor]) == 1:
                    leaves.append(neighbor)
        
        # The remaining nodes in the queue are the MHTs
        return list(leaves)