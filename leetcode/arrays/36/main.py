class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        def rowsValidate(board: list[list[str]]) -> bool:
            for row in board:
                vistos = set()
                for n in row:
                    if n == ".":
                        continue
                    if n in vistos:
                        return False
                    vistos.add(n)
            return True

        def columnsValidate(board: list[list[str]]) -> bool:
            for row in range(len(board)):
                vistos = set()
                for column in range(len(board)):
                    num = board[column][row]
                    if num == ".":
                        continue
                    if num in vistos:
                        return False
                    vistos.add(num)
            return True

        def boxesValidate(board: list[list[str]]) -> bool:
            starti = 0
            startj = 0
            count = 0
            while True:
                vistos = set()
                for i in range(starti, starti + 3):
                    for j in range(startj, startj + 3):
                        num = board[i][j]
                        if num == ".":
                            continue
                        if num in vistos:
                            return False
                        vistos.add(num)

                count += 1
                startj += 3

                if count == len(board):
                    return True
                if startj >= len(board):
                    starti += 3
                    startj = 0

        def sudokuValidate(board: list[list[str]]) -> bool:
            return (
                rowsValidate(board) and columnsValidate(board) and boxesValidate(board)
            )

        return sudokuValidate(board)


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["2", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", "2", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

print(Solution().isValidSudoku(board))
