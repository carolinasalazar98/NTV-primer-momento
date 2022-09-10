
fruta =[]

for i in range(2):
   fruta.append(input('Nombre de la fruta: '))
   fruta.append(input('Color de la fruta: '))
   fruta.append(int(input('Precio de la fruta: ')))
   

fruta.reverse()

for fruta in fruta: 
    print(fruta)

   
