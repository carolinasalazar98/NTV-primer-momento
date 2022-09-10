cantidad= (int(input("Digite la cantidad de numeros que desea ingresar: ")))
multiplo2= 0
multiplo3=0

for i in range(cantidad):
    numero=(int(input("Digite un numero: ")))

    if numero%2 == 0:
        multiplo2+=1
    if numero%3 == 0:
        multiplo3+=1

print(f"Numeros multiplos de 2: {multiplo2}") 
print(f"Numeros multiplos de 3: {multiplo3}")
