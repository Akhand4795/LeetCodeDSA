class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
       # Step 1: Construct an adjacency list representation of the tree
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        # Initialize arrays to store the number of nodes and distances for each node
        count = [0] * n  # Number of nodes in subtree rooted at each node
        ans = [0] * n    # Sum of distances from each node to all other nodes in subtree
        
        # Define a depth-first search (DFS) function
        def dfs(node, parent):
            nonlocal count, ans
            
            # Initialize count and answer for the current node
            count[node] = 1
            
            for neighbor in adj_list[node]:
                if neighbor != parent:
                    # Recursively traverse the subtree rooted at the neighbor
                    dfs(neighbor, node)
                    
                    # Update count and answer for the current node
                    count[node] += count[neighbor]
                    ans[node] += ans[neighbor] + count[neighbor]
        
        # Step 2: Perform DFS traversal starting from node 0 (root)
        dfs(0, -1)
        
        # Define a second DFS function to update distances for all nodes
        def dfs_update(node, parent):
            nonlocal count, ans
            
            for neighbor in adj_list[node]:
                if neighbor != parent:
                    # Update the answer for the neighbor based on the current node
                    ans[neighbor] = ans[node] - count[neighbor] + (n - count[neighbor])
                    
                    # Recursively traverse the subtree rooted at the neighbor
                    dfs_update(neighbor, node)
        
        # Step 3: Perform DFS traversal to update distances for all nodes
        dfs_update(0, -1)
        
        # Step 4: Construct the answer array
        return ans