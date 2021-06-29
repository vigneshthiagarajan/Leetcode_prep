class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        # store values (path location to avoid revisiting)
        path = set()

        def dfs(row, column, seek_char):
            if seek_char == len(word):
                return True
            if (
                row < 0
                or column < 0
                or row >= ROWS
                or column >= COLS
                or word[seek_char] != board[row][column]
                or (row, column) in path
            ):
                return False

            path.add((row, column))

            result = (
                (dfs(row + 1, column, seek_char + 1))
                or (dfs(row - 1, column, seek_char + 1))
                or (dfs(row, column + 1, seek_char + 1))
                or (dfs(row, column - 1, seek_char + 1))
            )

            path.remove((row, column))
            return result

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True
        return False
