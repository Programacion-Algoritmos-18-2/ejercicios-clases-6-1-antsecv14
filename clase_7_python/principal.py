# Importamos todas los metodos de las clases modelo y miarchivo

from modelado.modelo import *
from paquete_archivos.miarchivo import MiArchivo

# Creamos un objeto tipo MiArchivo y le mandamos la ubicacion de nuestro archivo

m = MiArchivo("data/datos.txt")

# En lista ingresamos los archivos del data
lista = m.obtener_informacion()

# Utilizamos el split para quitar la ","
lista = [l.split(",") for l in lista]

# Creamos un objeto tipo Convertir_lista y le enviamos la lista resultante del split

l = Convertir_lista(lista)

# Lista_para_busqueda va a ser igual a lista resultante del metodo lista_nueva

lista_para_busqueda = l.lista_nueva()

#Creamos un objeto tipo busqueda y le enviamos nuestra lista para busqueda

b = busqueda(lista_para_busqueda)

#Finalmente enviamos el atributo 11 al metodo busqueda_posicion para que asi el metodo
#nos devuelva la ubicacion

print("El numero buscado se encuentra en la posicion: ", b.busqueda_posicion(11))

#Cerramos el archivo

m.cerrar_archivo()