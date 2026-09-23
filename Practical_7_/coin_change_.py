def coin_change(N, coins):
    n = len(coins)

    dp = [[0 for j in range(N + 1)] for i in range(n + 1)]

    
    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, N + 1):

            
            if coins[i - 1] > j:
                dp[i][j] = dp[i - 1][j]

           
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]

    return dp[n][N]


N = int(input("Enter the amount: "))

n = int(input("Enter the number of coins: "))

coins = []

for i in range(n+1):
    x = int(input(f"Enter coin {i + 1}: "))
    coins.append(x)

result = coin_change(N, coins)

print("Number of ways:", result)