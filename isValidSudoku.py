def isValid(self, board):
        # code here
        seen = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:
                    if str(board[i][j])+'row'+str(i) not in seen: 
                        seen.add(str(board[i][j])+'row'+str(i))
                    else:
                        return 0
                    if (str(board[i][j])+'col'+str(j) not in seen):
                        seen.add(str(board[i][j])+'col'+str(j))
                    else:
                        return 0
                    if (str(board[i][j])+'box'+str(i//3)+str(j//3) not in seen):
                        seen.add(str(board[i][j])+'box'+str(i//3)+str(j//3))
                    else:
                        return 0
        return 1
