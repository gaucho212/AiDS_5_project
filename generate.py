import random

C = 20
n = 15


def generate_item():
    items = [(random.randint(1, 100), random.randint(1, 10)) for _ in range(n)]

    with open("knapsack_data.txt", "w") as f:
        f.write(f"{C}\n")
        f.write(f"{n}\n")
        for p, w in items:
            f.write(f"{p} {w}\n")
