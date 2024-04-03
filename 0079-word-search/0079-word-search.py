class Solution:
    def solve(self, board: List[List[str]], coords_set: Set[Tuple[int, int]], curr_i, curr_j, word, curr_idx) -> bool:
        if curr_idx == len(word):
            return True
        elif curr_idx > len(word):
            return False
        coords_set.add((curr_i, curr_j))
        next_coords = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        for (next_x, next_y) in next_coords:
            new_x = curr_i + next_x
            new_y = curr_j + next_y
            if new_x<len(board) and new_x>=0 and new_y<len(board[0]) and new_y>=0 and (new_x, new_y) not in coords_set and board[new_x][new_y] == word[curr_idx]:
                ret = self.solve(board, coords_set, new_x, new_y, word, curr_idx+1)
                if ret:
                    return True
        coords_set.remove((curr_i, curr_j))
        return False
        
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i_idx in range(len(board)):
            for j_idx in range(len(board[i_idx])):
                curr_char = board[i_idx][j_idx]
                if curr_char == word[0]:
                    coords_set = set()
                    ret = self.solve(board, coords_set, i_idx, j_idx, word, 1)
                    if ret:
                        return True
        return False
        