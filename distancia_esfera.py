from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import sys

#variables geograficas
latitud1 = float(sys.argv[2])
longitud1 = float(sys.argv[1])
latitud2 = float(sys.argv[4])
longitud2 =  float(sys.argv[3])
#variables esfericas
polar1 = np.pi/2-latitud1
azimut1 = longitud1
polar2 = np.pi/2-latitud2
azimut2 = longitud2
#radio de la tierra
R = 6371
#por la definicion de producto punto y la relacian angulo-arco-radio, se puede sacar el arco d entre ambos puntos
d1 = R*np.arccos(np.sin(polar1)*np.sin(polar2)*(np.cos(azimut1)*np.cos(azimut2) + np.sin(azimut1)*np.sin(azimut2)) 
                 + np.cos(polar1)*np.cos(polar2))
print "La distancia de la geodesica entre las dos ciudades es", d1, "Km"
