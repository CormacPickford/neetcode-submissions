class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row-wise
        for row in board:
            cov = []
            for i in row:
                if i in cov:
                    return False
                if i != '.':
                    cov.append(i)
        #col-wise
        cd = defaultdict(list)
        for row in range(len(board)):
            for column in range(len(board)):
                if column in cd and board[row][column] in cd[column]:
                    return False
                if board[row][column] != '.':
                    cd[column].append(board[row][column])
        sq = defaultdict()
        for row in range(len(board)):
            for column in range(len(board)):
                if row < 3 and column < 3:
                    if 0 in sq and board[row][column] in sq[0]:
                        return False
                    if board[row][column] != '.':
                        if 0 in sq:
                            sq[0].append(board[row][column])
                        else:
                            sq[0] = [board[row][column]]
                elif row <6 and column < 3:
                    if 1 in sq and board[row][column] in sq[1]:
                        return False
                    if board[row][column] != '.':
                        if 1 in sq:
                            sq[1].append(board[row][column])
                        else:
                            sq[1] = [board[row][column]]
                elif column < 3:
                    if  2 in sq and board[row][column] in sq[2]:
                        return False
                    if board[row][column] != '.':
                        if 2 in sq:
                            sq[2].append(board[row][column])
                        else:
                            sq[2] = [board[row][column]]
                elif row < 3 and column < 6:
                    if 3 in sq and board[row][column] in sq[3]:
                        return False
                    if board[row][column] != '.':
                        if 3 in sq:
                            sq[3].append(board[row][column])
                        else:
                            sq[3] = [board[row][column]]
                elif row <6 and column < 6:
                    if 4 in sq and board[row][column] in sq[4]:
                        return False
                    if board[row][column] != '.':
                        if 4 in sq:
                            sq[4].append(board[row][column])
                        else:
                            sq[4] = [board[row][column]]
                elif column < 6:
                    if 5 in sq and board[row][column] in sq[5]:
                        return False
                    if board[row][column] != '.':
                        if 5 in sq:
                            sq[5].append(board[row][column])
                        else:
                            sq[5] = [board[row][column]]
                elif row < 3:
                    if 6 in sq and board[row][column] in sq[6]:
                        return False
                    if board[row][column] != '.':
                        if 6 in sq:
                            sq[6].append(board[row][column])
                        else:
                            sq[6] = [board[row][column]]
                elif row < 6:
                    if 7 in sq and board[row][column] in sq[7]:
                        return False
                    if board[row][column] != '.':
                        if 7 in sq:
                            sq[7].append(board[row][column])
                        else:
                            sq[7] = [board[row][column]]
                else:
                    if 8 in sq and board[row][column] in sq[8]:
                        return False
                    if board[row][column] != '.':
                        if 8 in sq:
                            sq[8].append(board[row][column])
                        else:
                            sq[8] = [board[row][column]]
        return True


                
                
                




        
        