def palindromo(palabra):
    return palabra==palabra[::-1]

word = str(input("Ingrese una palabra para ver si es palindromo: ")).lower()
if palindromo(word):
    print("La palabra es palindromo")
else:
    print("La palabra no es palindromo")