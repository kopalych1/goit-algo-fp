ITEMS = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(budget: int):
    sorted_items = sorted(
        ITEMS.items(),
        key=lambda x: x[1]["calories"] / x[1]["cost"],
        reverse=True
    )

    selected = {}
    total_calories = 0
    remaining_budget = budget

    for name, data in sorted_items:
        if data["cost"] <= remaining_budget:
            selected[name] = 1
            remaining_budget -= data["cost"]
            total_calories += data["calories"]

    return selected, total_calories

def dynamic_programming(budget: int):
    names = list(ITEMS.keys())
    n = len(names)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        item = ITEMS[names[i - 1]]
        cost = item["cost"]
        calories = item["calories"]

        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    w = budget
    selected = {}

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name = names[i - 1]
            selected[name] = 1
            w -= ITEMS[name]["cost"]

    return selected, dp[n][budget]



def main():
    print(greedy_algorithm(50))
    print(dynamic_programming(50))
    print(greedy_algorithm(325))
    print(dynamic_programming(325))



if __name__ == "__main__":
    main()