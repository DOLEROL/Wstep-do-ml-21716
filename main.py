import numpy as np


# utwórz tablicę zawierającą 10 zer
print(f"Zad.1 \n"
      f"{np.zeros(10, dtype=int)}"
      f"\n")

# utwórz tablicę zawierającą 10 piątek,
a = np.arange(10, dtype=int)
print(f"Zad.2 \n"
      f"{np.full_like(a, 5)}"
      f"\n")

# utwórz tablicę zawierającą liczby od 10 do 50,
print(f"Zad.3 \n"
      f"{np.arange(10, 51)}"
      f"\n")

# utwórz macierz (tablica wielowymiarowa) o wymiarach 3x3 zawierającą liczby od 0 do 8,
print(f"Zad.4 \n"
      f"{np.arange(0, 9).reshape(3, 3)}"
      f"\n")

# utwórz macierz jednostkową o wymiarach 3x3,
print(f"Zad.5 \n"
      f"{np.identity(3)}"
      f"\n")

# utwórz macierz o wymiarach 5x5 zawierającą liczby z dystrybucji normalnej (Gaussa),
print(f"Zad.6 \n"
      f"{np.random.normal(size=25).reshape(5, 5)}"
      f"\n")

# utwórz macierz o wymiarach 10x10 zawierającą liczby od 0,01 do 1 z krokiem 0,01,
print(f"Zad.7 \n"
      f"{np.arange(0.01, 1.01, 0.01).reshape(10, 10)}"
      f"\n")

# utwórz tablicę zawierającą 20 liniowo rozłożonych liczb między 0 a 1 (włącznie z 0 i 1),
print(f"Zad.8 \n"
      f"{np.linspace(0, 1, 20)}"
      f"\n")

# utwórz tablicę zawierającą losowe liczby z przedziału (1, 25), następnie zamień ją na macierz o wymiarach 5 x 5 z tymi samymi liczbami:
arr = np.random.randint(1, 25, 25)
arr = arr.reshape(5, 5)
print(f"Zad.9.1 \n"
      f"{arr}"
      f"\n")

# ☻ oblicz sumę wszystkich liczb w ww. macierzy,
print(f"Zad.9.2 \n"
      f"{arr.sum()}"
      f"\n")

# ☻ oblicz średnią wszystkich liczb w ww. macierzy,
print(f"Zad.9.3 \n"
      f"{arr.sum() / arr.size}"
      f"\n")

# ☻ oblicz standardową dewiację dla liczb w ww. macierzy,
print(f"Zad.9.4 \n"
      f"{arr.std()}"
      f"\n")

# ☻ oblicz sumę każdej kolumny ww. macierzy i zapisz ją do tablicy.
arrColSum = arr.sum(axis=0)
print(f"Zad.9.5 \n"
      f"{arrColSum}"
      f"\n")

# utwórz macierz o wymiarach 5x5 zawierającą losowe liczby z przedziału (0, 100) oraz:
arr_10 = np.random.randint(0, 100, 25).reshape(5, 5)
print(f"Zad.10 \n"
      f"{arr_10}"
      f"\n")

# ☻ oblicz medianę tych liczb,
arr_10_1 = np.median(arr_10)
print(f"Zad.10_1 \n"
      f"{arr_10_1}"
      f"\n")

# ☻ znajdź najmniejszą liczbę tej macierzy,
arr_10_2 = np.amin(arr_10)
print(f"Zad.10_2 \n"
      f"{arr_10_2}"
      f"\n")

# ☻ znajdź największą liczbę tej macierzy.
arr_10_3 = np.amax(arr_10)
print(f"Zad.10_3 \n"
      f"{arr_10_3}"
      f"\n")

# utwórz macierz o wymiarach różnych od siebie i większych od 1, zawierającą losowe liczby z przedziału (0, 100) i dokonaj jej transpozycji,
arr_11 = np.random.randint(0, 100, 20).reshape(4, 5)
print(f"Zad.11 \n"
      f"{arr_11}"
      f"\n")
arr_11 = np.transpose(arr_11)
print(f""
      f"{arr_11}"
      f"\n")

# utwórz dwie macierze o odpowiednich wymiarach, większych od 2x2 i dodaj je do siebie,
arr_12_1 = np.random.randint(0, 10, 9).reshape(3, 3)
arr_12_2 = np.random.randint(0, 10, 9).reshape(3, 3)
arr_12_sum = np.add(arr_12_1, arr_12_2)

print(f"Zad.12 \n"
      f"{arr_12_1}"
      f"\n")

print(f""
      f"{arr_12_2}"
      f"\n")

print(f""
      f"{arr_12_sum}"
      f"\n")

# utwórz dwie macierze o odpowiednich wymiarach różnych od siebie i większych od 2, a następnie pomnóż je przez siebie za pomocą dwóch różnych funkcji (np. ‘matmul’ i ‘multiply’, proszę poczytać o różnicach w obliczaniu wyników mnożenia).
arr_13_1 = np.random.randint(0, 10, 12).reshape(3, 4)
arr_13_2 = np.random.randint(0, 10, 4)
arr_13_1_mul = np.matmul(arr_13_1, arr_13_2)
arr_13_2_mul = np.multiply(arr_13_1, arr_13_2)

print(f"Zad.13 \n"
      f"{arr_13_1}"
      f"\n")

print(f""
      f"{arr_13_2}"
      f"\n")

print(f""
      f"{arr_13_1_mul}"
      f"\n")

print(f""
      f"{arr_13_2_mul}"
      f"\n")
