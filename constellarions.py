import matplotlib.pyplot as plt

class star:
    def __init__(self, x, y, id,HRN, name=None) :
        self.x = x
        self.y = y
        self.id=id
        self.HRN= HRN #Harvard Revised Number
        self.name = name


stars=[]
with open('stars.txt', 'r') as archivo:
    # Leer cada línea del archivo y hacer split por espacio
    for linea in archivo:
        datos = linea.split()
        nombres= []
        if len(datos) >6:
            ind= 6
            while ind < len(datos):
                nombres.append(datos[ind])
                ind+=1
        Star = star(datos[0], datos[1], datos[3],datos[5], nombres)
        stars.append(Star)
        
coor_x=[x.x for x in stars]
coor_y=[y.y for y in stars]

fig, ax = plt.subplots()

# Establecer el color de fondo
ax.set_facecolor('#0e2238')

ax.scatter(coor_x,coor_y)

# Mostrar el gráfico
plt.show()