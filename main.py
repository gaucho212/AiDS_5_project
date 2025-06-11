from item import Item
from knapsack import Knapsack
from generate import generate_item
import sys


def read_knapsack_data(filename):
    with open(filename, "r") as f:
        C = int(f.readline().strip())
        n = int(f.readline().strip())
        items = []
        for _ in range(n):
            p, w = map(int, f.readline().strip().split())
            items.append(Item(p, w))
    return Knapsack(C, items)


if __name__ == "__main__":
    action = ""
    generate_item()
    try:
        knapsack = read_knapsack_data("knapsack_data.txt")
    except FileNotFoundError:
        print(
            "Plik 'knapsack_data.txt' nie został znaleziony. Upewnij się, że plik istnieje."
        )
        sys.exit(1)
    while True:
        print("action> ", end="")
        action = input().strip()
        if action.lower() == "print":
            print("Dane plecaka:")
            print(f"Pojemność: {knapsack.capacity}")
            print(f"Liczba przedmiotów: {len(knapsack.items)}")
            print("Przedmioty (wartość, waga):")
            for i, item in enumerate(knapsack.items):
                try:
                    print(f"  {i}: ({item.value}, {item.weight})")
                except AttributeError as e:
                    print(f"  Błąd odczytu przedmiotu {i}: {e}")

        elif action.lower() == "dynamic":
            print("Rozwiązanie metodą programowania dynamicznego:")
            dp_value, dp_items = knapsack.dynamic_programming()
            print(f"Maksymalna wartość: {dp_value}")
            print("Wybrane przedmioty (indeksy):", dp_items)
        elif action.lower() == "brute":
            print("\nRozwiązanie metodą siłową:")
            bf_value, bf_items = knapsack.brute_force()
            print(f"Maksymalna wartość: {bf_value}")
            print("Wybrane przedmioty (indeksy):", bf_items)
        elif action.lower() == "exit":
            sys.exit(0)
        elif action.lower() == "help":
            print("Dostępne komendy:")
            print("  print - wyświetla dane plecaka")
            print("  dynamic - rozwiązuje problem metodą programowania dynamicznego")
            print("  brute - rozwiązuje problem metodą siłową")
            print("  exit - kończy program")
            print("  help - wyświetla tę pomoc") 
        else:
            print("Nieznana komenda. Wpisz 'help' aby zobaczyć dostępne komendy.")
        print()
