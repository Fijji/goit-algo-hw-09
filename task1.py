import time

coins = [50, 25, 10, 5, 2, 1]
amounts_to_test = [113, 256, 512, 1000, 3336]

def find_coins_greedy(amount):
    result = {}
    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count
    return result

def find_min_coins(amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)
    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    result = {}
    while amount > 0:
        result[coin_used[amount]] = result.get(coin_used[amount], 0) + 1
        amount -= coin_used[amount]
    return result

def measure_time(func, amount):
    start_time = time.time()
    result = func(amount)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time, result

print("Порівняння алгоритмів:")
for amount in amounts_to_test:
    time_greedy, result_greedy = measure_time(find_coins_greedy, amount)
    time_dynamic, result_dynamic = measure_time(find_min_coins, amount)
    print(f"Для суми {amount}:")
    print(f"Жадібний: {result_greedy}, час: {time_greedy} секунд")
    print(f"Динамічний: {result_dynamic}, час: {time_dynamic} секунд")
    print()
