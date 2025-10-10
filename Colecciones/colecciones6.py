cadena = input("Dame una cadena de texto: ")
d = cadena.split()
print(d)

frecuencia = d = {palabra: d.count(palabra) for palabra in d}
for palabra, cuenta in frecuencia.items():
    print(f"La palabra '{palabra}' aparece {cuenta} veces")