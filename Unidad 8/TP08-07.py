"""
-----------------------------------------------------------------------------------------------
Título: CLAVE ENTERO Y VALOR ENTERO AL CUADRADO

Fecha: 04/12/23

Autor: Gianfranco Mazzei

Descripción: Generar e imprimir un diccionario donde las claves sean números enteros entre 1 y 20 (ambos incluidos) y los valores 
asociados sean el cuadrado de las claves.

Pendientes:

-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
...


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
...

        
#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables y entrada de datos
#-------------------------------------------------

conjunto = {}
listaClaves = []
listaValores = []

#-------------------------------------------------
# Procesos
#-------------------------------------------------

for clave in range(0,20):
    listaClaves.append(clave)
    cuadrado = clave ** 2
    listaValores.append(cuadrado)

conjunto = dict(zip(listaClaves, listaValores))

#-------------------------------------------------
# Resultados
#-------------------------------------------------

print(conjunto)
