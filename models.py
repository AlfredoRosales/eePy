import sqlite3
miConexion=sqlite3.connect('SegundaBase')
miCursor=miConexion.cursor()

""" miCursor.execute('''
    CREATE TABLE PRODUCTOS(
        CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,  #Llave Primaria
        NOMBRE_ARTICULO VARCHAR(50),
        PRECIO INTEGER,
        SECCION VARCHAR(20)
    )  
''') """

""" productos=[
    ('AR01','Pelota',20,'Juguetería'),
    ('AR02','Pantalón',15,'Confección'),
    ('AR03','Destornillador',25,'Ferretería'),
    ('AR04','Jarrón',45,'Cerámica')
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", productos) """

miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR05','Tren',15,'Juguetería')")


miConexion.commit()
miConexion.close()
