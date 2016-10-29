# coding=utf-8


# 面试题20：顺时针打印矩阵
def print_matrix_clock_wisely(matrix):
    # row
    n = len(matrix)
    # column
    m = len(matrix[0])

    start = 0
    while start <= n/2 and start <= m/2:
        # i = j = start
        # while j < m-start:
        #     print matrix[i][j]
        #     j += 1
        # j -= 1
        # i += 1
        # if i >=n-start:
        #     break
        # while i < n-start:
        #     print matrix[i][j]
        #     i += 1
        # i -= 1
        # j -= 1
        # if j < start:
        #     break
        # while j >= start:
        #     print matrix[i][j]
        #     j -= 1
        # j += 1
        # i -= 1
        # if i <= start:
        #     break
        # while i > start:
        #     print matrix[i][j]
        #     i -= 1

        # from left to right
        for i in range(start, m-start):
            print matrix[start][i]
        # from top to low
        if start < m - start - 1:
            for i in range(start+1, n-start):
                print matrix[i][m-start-1]
        # from right to left
        if start < m - start - 1 and start < n - start - 1:
            for i in range(m-start-2, start-1, -1):
                print matrix[n-start-1][i]
        # from low to top
        if start < m - start - 1 and start+1 < n - start - 1:
            for i in range(n-start-2, start, -1):
                print matrix[i][start]
        start += 1

if __name__ == "__main__":
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    matrix11 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
    matrix12 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
    matrix13 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

    matrix2 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
    print_matrix_clock_wisely(matrix13)