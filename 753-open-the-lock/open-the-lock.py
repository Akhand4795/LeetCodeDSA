class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends_set = set(deadends)
        if "0000" in deadends_set:
            return -1
        
        queue = deque(["0000"])
        visited = set(["0000"])
        moves = 0
        
        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                if current == target:
                    return moves
                if current in deadends_set:
                    continue
                for i in range(4):
                    for d in [-1, 1]:
                        new_digit = (int(current[i]) + d) % 10
                        new_state = current[:i] + str(new_digit) + current[i+1:]
                        if new_state not in visited:
                            queue.append(new_state)
                            visited.add(new_state)
            moves += 1
        
        return -1