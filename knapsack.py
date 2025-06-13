from itertools import product

class Knapsack:
    def __init__(self, capacity, items):
        self.capacity = capacity
        self.items = items  # lista obiektów Item

    def dynamic_programming(self):
        n = len(self.items)
        dp = [[0] * (self.capacity + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for w in range(self.capacity + 1):
                if self.items[i - 1].weight > w:
                    dp[i][w] = dp[i - 1][w]
                else:
                    dp[i][w] = max(
                        dp[i - 1][w],
                        dp[i - 1][w - self.items[i - 1].weight]
                        + self.items[i - 1].value,
                    )

        # Cofanie się, aby znaleźć wybrane przedmioty
        included_items = []
        w = self.capacity
        for i in range(n, 0, -1):
            if dp[i][w] != dp[i - 1][w]:
                included_items.append(i - 1)
                w -= self.items[i - 1].weight

        included_items.reverse()
        return dp[n][self.capacity], included_items

    def brute_force(self):

        n = len(self.items)
        max_value = 0
        best_subset = []

        for bits in product([0, 1], repeat=n):
            total_weight = 0
            total_value = 0
            subset = []
            for i in range(n):
                if bits[i]:
                    total_weight += self.items[i].weight
                    total_value += self.items[i].value
                    subset.append(i)
            if total_weight <= self.capacity and total_value > max_value:
                max_value = total_value
                best_subset = subset

        return max_value, best_subset
