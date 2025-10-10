d = {
    "e": "p",
    "i": "v",
    "k": "i",
    "m": "u",
    "p": "m",
    "q": "t",
    "r": "e",
    "s": "r",
    "t": "k",
    "u": "q",
    "v": "s"
}

frase = input("Introduce una frase: ")
frase_encriptada = ''.join(d.get(char, char) for char in frase)
print("Frase encriptada:", frase_encriptada)