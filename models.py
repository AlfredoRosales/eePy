import sqlite3
miConexion=sqlite3.connect('TerceraBase')
miCursor=miConexion.cursor()

#PK incremental (por default es UNIQUE)
""" miCursor.execute('''
    CREATE TABLE PRODUCTOS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT, 
        NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
        PRECIO INTEGER,
        SECCION VARCHAR(20)
    )  
''') """
### CREATE ###
""" productos=[
    ('Pelota',20,'Juguetería'),
    ('Pantalón',15,'Confección'),
    ('Destornillador',25,'Ferretería'),
    ('Jarrón',45,'Cerámica')
] """

#miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)
# miCursor.execute("INSERT INTO PRODUCTOS VALUES (Null,'Tren',15,'Juguetería')") # Agregar solo un registro

### CONSULTA ###
# miCursor.execute("SELECT * FROM PRODUCTOS WHERE  SECCION='Confección'")  # Key Sensitive!!!!
#productos=miCursor.fetchall()
#print(productos)


### UPDATE ###

#miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='Pelota'")

### DELETE ###

#miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")


miConexion.commit()
miConexion.close()
