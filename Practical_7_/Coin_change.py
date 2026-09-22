def coin_change(coins, amount):
    dp = [0] + [999] * amount

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount]


n = int(input("Enter number of coins: "))

coins = []
for i in range(n):
    coin = int(input("Enter coin: "))
    coins.append(coin)

amount = int(input("Enter amount: "))


answer = coin_change(coins, amount)

print("Minimum number of coins:", answer)