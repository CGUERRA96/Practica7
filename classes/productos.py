import os

class Productos:
    def __init__(self, nombre, cantidad, costo):
        self.nombre = nombre
        self.cantidad = cantidad
        self.costo = costo

    @staticmethod

    def ingresar_productos(conn, data):
        productos = []
        for i in data:
            costo_total = i.cantidad * i.costo
            insert = {
                'productos': i.nombre,
                'Cantidad_Dsiponible': i.cantidad,
                'Costo_Neto': i.costo,
                'Costo_Total': costo_total
            }
            productos.append(insert)
        
        if productos:
            conn.insertar_registros('productos', productos)

    @staticmethod
    def generar_reporte(conn):
        productos = conn.obtener_registros('productos')
        try:
            file = open('productos.txt', 'w')
            fila_productos = ''
            n = 1
            for i in productos:
                fila_productos += f'Nro {n}, Nombre: {i["productos"]}, Cantidad: {i["Cantidad_Dsiponible"]}, Costo Neto: {i["Costo_Neto"]}, Costo Total: {i["Costo_Total"]}\n'
                n += 1
            file.write(fila_productos)
            print('Se genero reporte de productos')
        except Exception as e:
            print(f'{str(e)}')
        finally:
            if file:
                file.close()
        
