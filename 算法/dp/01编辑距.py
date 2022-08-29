# dp完成编辑距算法

def edit_distance(str1, str2):
    n = len(str1)
    m = len(str2)
    dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
    
    # 填表
    for i in range(0, n + 1):
        for j in range(0, m + 1):
            if i == 0:
                dp[0][j] = j
            if j == 0:
                dp[i][0] = i
            if i != 0 and j != 0:
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[n][m]


str1 = "xxix"
str2 = "xxix"
print(edit_distance(str1, str2))



