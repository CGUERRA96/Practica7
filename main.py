from connection.conn import Conexion
from classes.productos import Productos

conn = Conexion('mongodb://localhost:27017','Market')

try:
    lista_productos = []
    nro_productos = int(input('Ingrese el nro de productos: '))

    while True:
        for i in range(nro_productos):
            nombre = input(f'Ingrese el nombre del Producto n°{i + 1} : ')
            cantidad = int(input(f'Cantidad para el producto {nombre} : '))
            costo = float(input(f'Cuanto cuesta el producto {nombre}? : '))
            producto = Productos(nombre, cantidad, costo)
            lista_productos.append(producto)
        
        print(lista_productos)

        if lista_productos:
            Productos.ingresar_productos(conn, lista_productos)
        break
except Exception as e:
    print(f'{str(e)}')