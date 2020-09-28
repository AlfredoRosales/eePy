import sqlite3
miConexion=sqlite3.connect('PrimeraBase') # Se crea la base de datos
miCursor=miConexion.cursor()        # Se crea el puntero


## CREATE
#miCursor.execute("CREATE TABLE PRODUCTOS(NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER, SECCION VARCHAR(20))") Se crea la tabla
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN',15,'DEPORTES')") # Insertando registro

""" variosProductos=[                   # Estos registros están en una TUPLA
    ('Camiseta',10,'Deportes'),
    ('Jarrón',10,'Cerámica'),
    ('Camión',10,'Juguetería')
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)",variosProductos)  # Se inserta lote de registros """

## READ
miCursor.execute("SELECT * FROM PRODUCTOS")  # Consulta de lectura

variosArticulos=miCursor.fetchall()     # Importa todos los registros de la BB.DD en una tupla (variosArticulos)
#print(variosArticulos)                 # Imprime todos los registros (método 1) (todo el contenido de la Tupla)

for producto in variosArticulos:        # Imprime todos los registros (método 2) (en vertical por el print, sin corchete)
    print(producto)


miConexion.commit() # Se confirma la inserción del nuevo registro
miConexion.close()
