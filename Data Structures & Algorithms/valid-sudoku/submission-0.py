class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box_values = []

        for i in range(0, 9):
            row_values = [value for value in board[i] if value != "."]
            row_set = set(row_values)
            if len(row_set) != len(row_values):
                return False

            column_values = [board[j][i] for j in range(0, 9) if board[j][i] != "."]
            column_set = set(column_values)
            if len(column_values) != len(column_set):
                return False
        
        for l in range(0, 9, 3):
            for t in range(0, 9, 3):
                for n in range(l, l + 3):
                    for m in range(t, t + 3):
                    
                        if board[n][m] != ".":
                            box_values.append(board[n][m])
                box_set = set(box_values)
                if len(box_values) != len(box_set):
                    return False
                else:
                    box_values = []
        return True