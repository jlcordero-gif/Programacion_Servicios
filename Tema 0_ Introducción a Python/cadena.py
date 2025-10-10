#el puesto 8 de la cadena no lo coge
long_string = "examples of long string"

print (long_string[5])
print (long_string[4:8])

#coge los valores de 2 en 2
print (long_string[2:12:2])

#separa la cadena por el caracter
print (long_string.split("e"))

#une la cadena
words =["string", "whith", "words"]
new_phrase = "-".join (words)
print(new_phrase)

#revertir frase
print(long_string[::-1])