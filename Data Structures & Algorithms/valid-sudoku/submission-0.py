class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowseen = [set()for _ in range(9)]
        columnseen = [set() for _ in range(9)]
        subseen = [set() for _ in range(9)]

        for i  in range(len(board)):
            for j in range(len(board)):
                if board[i][j] in rowseen[i]:
                    if board[i][j] != "." :
                        return False
                else:
                    rowseen[i].add(board[i][j])

                if board[i][j] in columnseen[j]:
                    if board[i][j] == ".":
                        continue
                    else:
                        return False
                else:
                    columnseen[j].add(board[i][j])

                subnum = i//3 * 3 + j//3
                if board[i][j] in subseen[subnum]:
                    if board[i][j] == ".":
                        continue
                    else:
                        return False
                else:
                    subseen[subnum].add(board[i][j])

        return True

        

        
