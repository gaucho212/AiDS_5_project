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
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - self.items[i - 1].weight] + self.items[i - 1].value)

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
        max_value = 0
        best_subset = []

        def recurse(index, current_weight, current_value, current_subset):
            nonlocal max_value, best_subset
            if index == len(self.items):
                if current_weight <= self.capacity and current_value > max_value:
                    max_value = current_value
                    best_subset = current_subset[:]
                return
            # Pominięcie przedmiotu
            recurse(index + 1, current_weight, current_value, current_subset)
            # Włączenie przedmiotu, jeśli się mieści
            if current_weight + self.items[index].weight <= self.capacity:
                recurse(index + 1, current_weight + self.items[index].weight, current_value + self.items[index].value, current_subset + [index])

        recurse(0, 0, 0, [])
        return max_value, best_subset