"""Abrir un video de Youtube con Python"""

import pywhatkit


try:
    pywhatkit.playonyt("villancico dulce jesus mio") #playonyt => play on Youtube
    print("cargando video")

except:
    print("Ha ocurrido un error!")
 