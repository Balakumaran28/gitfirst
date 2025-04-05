# 1. Sudoku Solver
def solve_sudoku(board):
    def solve(board):
        empty = find_empty(board)
        if not empty:
            return True
        row, col = empty
        for i in range(1, 10):
            if valid(board, i, (row, col)):
                board[row][col] = i
                if solve(board):
                    return True
                board[row][col] = 0
        return False

    def valid(board, num, pos):
        for i in range(9):
            if board[pos[0]][i] == num and pos[1] != i:
                return False
        for i in range(9):
            if board[i][pos[1]] == num and pos[0] != i:
                return False
        box_x, box_y = pos[1]//3, pos[0]//3
        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x*3, box_x*3 + 3):
                if board[i][j] == num and (i,j) != pos:
                    return False
        return True

    def find_empty(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)
        return None

    solve(board)


# 2. N-Queens Solver
def solve_n_queens(n):
    res = []
    board = [-1]*n

    def dfs(row):
        if row == n:
            res.append(board[:])
            return
        for col in range(n):
            if all(board[i] != col and abs(board[i]-col) != row-i for i in range(row)):
                board[row] = col
                dfs(row + 1)

    dfs(0)
    return res


# 3. Word Ladder (BFS)
from collections import deque
def word_ladder(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0
    q = deque([(beginWord, 1)])
    while q:
        word, level = q.popleft()
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                newWord = word[:i] + c + word[i+1:]
                if newWord == endWord:
                    return level + 1
                if newWord in wordSet:
                    wordSet.remove(newWord)
                    q.append((newWord, level + 1))
    return 0


# 4. Longest Valid Parentheses
def longest_valid_parentheses(s):
    stack = [-1]
    max_len = 0
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])
    return max_len


# 5. K-th Permutation
import math
def get_kth_permutation(n, k):
    nums = list(map(str, range(1, n+1)))
    k -= 1
    res = ''
    for i in range(n):
        fact = math.factorial(n-1-i)
        res += nums.pop(k // fact)
        k %= fact
    return res


# 6. Largest Rectangle in Histogram
def largest_rectangle_area(heights):
    stack, max_area = [], 0
    heights.append(0)
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            H = heights[stack.pop()]
            W = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, H * W)
        stack.append(i)
    return max_area


# 7. Trapping Rain Water
def trap_rain_water(height):
    if not height:
        return 0
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water
