"""2. Definir función, parámetros, retorno,
capturar un valor o varios"""

def mate(prefer):
    counta = 0
    countd = 0
    for i in prefer:
        if i=="amargo":
            counta+=1
        elif i=="dulce":
            countd+=1
    if(counta>countd):
        return print(f"El mejor mate es el amargo")
    elif (countd>counta):
        return print(f"El mejor mate es el dulce")

mejor = mate(["amargo","dulce","amargo","dulce","amargo"])