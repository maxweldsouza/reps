# ctci 16.4
import unittest

def tictacwin(board):
    score = {'X': 0, 'Y': 0, ' ': 0}
    def match(a, b, c):
        if a == b == c:
            score[a] += 1
    for i in range(3):
        match(*board[i])
    transpose = zip(*board)
    for i in range(3):
        match(*transpose[i])
    match(board[0][0], board[1][1], board[2][2])
    match(board[0][2], board[1][1], board[2][0])
    if score['X'] > 0 and score['Y'] > 0:
        raise ValueError('Invalid input')
    elif score['X'] > 0:
        return 'X'
    elif score['Y'] > 0:
        return 'Y'
    else:
        return None

print tictacwin([('X', ' ', ' '),(' ', ' ', ' '),(' ', ' ', ' ')])
print tictacwin([('X', 'Y', ' '),(' ', ' ', ' '),(' ', ' ', ' ')])
print tictacwin([('X', 'X', 'X'),(' ', ' ', ' '),(' ', ' ', ' ')])
print tictacwin([('X', ' ', ' '),('X', ' ', ' '),('X', ' ', ' ')])
print tictacwin([('X', ' ', ' '),(' ', 'X', ' '),(' ', ' ', 'X')])
print tictacwin([(' ', ' ', 'X'),(' ', 'X', ' '),('X', ' ', ' ')])
print tictacwin([('Y', 'Y', 'Y'),(' ', ' ', ' '),(' ', ' ', ' ')])
print tictacwin([('Y', ' ', ' '),('Y', ' ', ' '),('Y', ' ', ' ')])
print tictacwin([('Y', ' ', ' '),(' ', 'Y', ' '),(' ', ' ', 'Y')])
print tictacwin([(' ', ' ', 'Y'),(' ', 'Y', ' '),('Y', ' ', ' ')])
