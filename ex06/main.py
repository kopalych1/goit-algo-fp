import random
import matplotlib.pyplot as plt

def monte_carlo_dice(n: int):
    counts = {i: 0 for i in range(2, 13)}

    for _ in range(n):
        dice_sum = random.randint(1, 6) + random.randint(1, 6)
        counts[dice_sum] += 1

    probabilities = {k: v/n for k, v in counts.items()}
    return probabilities


def main():
    analytical = {2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 
              7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36}

    monte_carlo = monte_carlo_dice(100_000)

    print(f"{'Sum':<6} {'Monte carlo':<15} {'Analytical':<15} {'Difference':<10}")
    print("-" * 50)
    for s in range(2, 13):
        diff = abs(monte_carlo[s] - analytical[s])
        print(f"{s:<6} {monte_carlo[s]:<15.4f} {analytical[s]:<15.4f} {diff:<10.6f}")

    sums = list(range(2, 13))
    plt.figure(figsize=(10, 6))
    plt.bar([s - 0.2 for s in sums], [monte_carlo[s] for s in sums], 
            width=0.4, label='Monte carlo', alpha=0.8)
    plt.bar([s + 0.2 for s in sums], [analytical[s] for s in sums], 
            width=0.4, label='Analytical', alpha=0.8)
    plt.xlabel('Sum')
    plt.ylabel('Probability')
    plt.legend()
    plt.grid(alpha=0.3)
    plt.show()


if __name__ == "__main__":
    main()