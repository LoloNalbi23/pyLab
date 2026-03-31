
mayusc = False # Contiene al menos una letra mayúscula
minusc = False # y una letra minúscula.
num = False # Tiene al menos un número.
especial = False # Tiene al menos un carácter especial (por ejemplo, !, @, #, $, %, etc.).
largo = False #Tiene al menos 8 caracteres de longitud.
pswd = input('Ingrese su contraseña: ')

if len(pswd)>= 8:
    largo = True
    for i in pswd:
        if i.isupper():
            mayusc = True
        elif i.islower():
            minusc = True
        elif i.isdigit():
            num = True
        elif not i.isalnum():
            especial = True

#Informa al usuario si la contraseña es válida o no.
if largo and mayusc and minusc and num and especial:
    print('Contraseña valida')
else:
    print('Contraseña invalida')