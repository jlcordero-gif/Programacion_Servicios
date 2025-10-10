d = {
    "A": 1, "E": 1, "O": 1, "S": 1, "I": 1, "U": 1, "N": 1, "R": 1, "T": 1,
    "D": 2, "G": 2, "L": 2,
    "C": 3, "M": 3, "B": 3, "P": 3,
    "F": 4, "H": 4, "V": 4, "Y": 4,
    "Q": 5,
    "J": 8, "Ñ": 8, "X": 8,
    "K": 10, "Z": 10
}

palabra = input("Dame una palabra: ").upper()
puntuacion = sum(d.get(letra, 0) for letra in palabra)
print(f"La puntuación de la palabra '{palabra}' es: {puntuacion}")