class Solution:
    def isValidRow(self, board: List[List[str]], n) -> bool:
        row = set()
        for i in range(9):
            if board[n][i] in row and board[n][i].isdigit():
                return False
            row.add(board[n][i])
        return True
            


    def isValidColumn(self, board: List[List[str]], m) -> bool:
        col = set()
        for i in range(9):
            if board[i][m] in col and board[i][m].isdigit():
                return False
            col.add(board[i][m])
        return True
    
    def isValidSquare(self, board: List[List[str]], n,m) -> bool:
        square = set()
        for i in range(3):
            for j in range(3):
                if board[n+i][m+j] in square and board[n+i][m+j].isdigit():
                    return False
                square.add(board[n+i][m+j])

        return True




    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not self.isValidRow(board, i):
                return False
            if not self.isValidColumn(board, i):
                return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.isValidSquare(board, i, j):
                    return False
        
        return True
        