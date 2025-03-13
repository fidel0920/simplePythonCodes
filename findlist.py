
mi_lista = [1, 2, 3, 4, 5, 15]
elemento_a_buscar = 156


encontrado = False
for elemento in mi_lista:
    if elemento == elemento_a_buscar:
        encontrado = True
        break  


if encontrado:
    print(f"El elemento {elemento_a_buscar} está en la lista.")
else:
    print(f"El elemento {elemento_a_buscar} no está en la lista.")

