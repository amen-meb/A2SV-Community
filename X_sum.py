def max_bishop_sum(n, m, board):
    def diagonal_sum(x, y):
        total = board[x][y]

        i, j = x - 1, y - 1
        while i >= 0 and j >= 0:
            total += board[i][j]
            i -= 1
            j -= 1

        i, j = x - 1, y + 1
        while i >= 0 and j < m:
            total += board[i][j]
            i -= 1
            j += 1

        i, j = x + 1, y - 1
        while i < n and j >= 0:
            total += board[i][j]
            i += 1
            j -= 1

        i, j = x + 1, y + 1
        while i < n and j < m:
            total += board[i][j]
            i += 1
            j += 1
            
        return total

    max_sum = 0
    for i in range(n):
        for j in range(m):
            max_sum = max(max_sum, diagonal_sum(i, j))
    
    return max_sum


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    print(max_bishop_sum(n, m, board))
