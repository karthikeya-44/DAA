
n = int(input("Enter number of items: "))

weights = []
values = []

print("Enter weights:")
for i in range(n):
    weights.append(int(input(f"Weight of item {i + 1}: ")))

print("Enter values:")
for i in range(n):
    values.append(int(input(f"Value of item {i + 1}: ")))

capacity = int(input("Enter capacity of knapsack: "))

dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for w in range(1, capacity + 1):

        if weights[i - 1] <= w:
            dp[i][w] = max(
                values[i - 1] + dp[i - 1][w - weights[i - 1]],
                dp[i - 1][w]
            )
        else:
            dp[i][w] = dp[i - 1][w]

print("Maximum value =", dp[n][capacity])