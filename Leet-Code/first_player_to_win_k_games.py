from collections import deque

class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        if k >= n:
            return skills.index(max(skills))

        queue = deque(range(n))
        current_winner_index = queue.popleft()
        win_count = 0

        while win_count < k:
            next_player_index = queue.popleft()

            if skills[current_winner_index] > skills[next_player_index]:
                win_count += 1
                queue.append(next_player_index)
            else:
                current_winner_index = next_player_index
                win_count = 1
                queue.append(current_winner_index)

        return current_winner_index