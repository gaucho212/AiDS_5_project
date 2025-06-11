import pandas as pd  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
from matplotlib.backends.backend_pdf import PdfPages  # type: ignore

# Wczytanie danych z plików CSV
results_n = pd.read_csv("results.csv")
results_c = pd.read_csv("results2.csv")

# Ustawienie stylu wykresów
plt.style.use("seaborn-v0_8")
# Sprawdzenie poprawności wczytanych danych
print("Podgląd danych results_n:")
print(results_n.head())
print("\nPodgląd danych results_c:")
print(results_c.head())
# Tworzenie wykresu t=f(n) dla stałego C
plt.figure(figsize=(10, 6))
plt.plot(
    results_n["n"],
    results_n["dynamic_time"],
    label="Programowanie dynamiczne",
    marker="o",
    color="green",
)
plt.plot(
    results_n["n"],
    results_n["brute_time"],
    label="Brute Force",
    marker="o",
    color="red",
)
plt.xlabel("Liczba przedmiotów (n)")
plt.ylabel("Czas wykonania (s)")
plt.title("Czas wykonania w zależności od liczby przedmiotów (stałe C)")
plt.legend()
plt.grid(True)

# Zapisanie wykresów do PDF
with PdfPages("wykresy.pdf") as pdf:
    pdf.savefig()  # Zapisuje pierwszy wykres
    plt.close()

    # Tworzenie wykresu t=f(C) dla stałego n
    plt.figure(figsize=(10, 6))
    plt.plot(
        results_c["C"],
        results_c["dynamic_time"],
        label="Programowanie dynamiczne",
        marker="o",
        color="green",
    )
    plt.plot(
        results_c["C"],
        results_c["brute_time"],
        label="Brute Force",
        marker="o",
        color="red",
    )
    plt.xlabel("Pojemność plecaka (C)")
    plt.ylabel("Czas wykonania (s)")
    plt.title("Czas wykonania w zależności od pojemności plecaka (stałe n)")
    plt.legend()
    plt.grid(True)
    pdf.savefig()  # Zapisuje drugi wykres
    plt.close()

print("Wykresy zostały zapisane do pliku knapsack_analysis.pdf")
