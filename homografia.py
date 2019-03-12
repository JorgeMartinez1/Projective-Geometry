""" Funcion para hallar la homografia a partir de 4 puntos """

import numpy as np

def hmgrafia4puntos(coo_original,coo_deseada):
    # Se toman los puntos de la imagen deseada
    x1, y1 = coo_deseada[0], coo_deseada[1]
    x2, y2 = coo_deseada[2], coo_deseada[3]
    x3, y3 = coo_deseada[4], coo_deseada[5]
    x4, y4 = coo_deseada[6], coo_deseada[7]
    
    
    # Se toman los puntos de la imagen original
    xp1, yp1 = coo_original[0], coo_original[1]
    xp2, yp2 = coo_original[2], coo_original[3]
    xp3, yp3 = coo_original[4], coo_original[5]
    xp4, yp4 = coo_original[6], coo_original[7]
    
    # Sistema lineal para hallar h.
    A = np.array([
            [x1,y1,1,0,0,0,(-xp1*x1),(-xp1*y1)],[0,0,0,x1,y1,1,(-yp1*x1),(-yp1*y1)],
            [x2,y2,1,0,0,0,(-xp2*x2),(-xp2*y2)],[0,0,0,x2,y2,1,(-yp2*x2),(-yp2*y2)],
            [x3,y3,1,0,0,0,(-xp3*x3),(-xp3*y3)],[0,0,0,x3,y3,1,(-yp3*x3),(-yp3*y3)],
            [x4,y4,1,0,0,0,(-xp4*x4),(-xp4*y4)],[0,0,0,x4,y4,1,(-yp4*x4),(-yp4*y4)]])
    
    b = np.array([[xp1],[yp1],[xp2],[yp2],[xp3],[yp3],[xp4],[yp4]])
    
    # Descomposicion de valores singulares
    U, s, V = np.linalg.svd(A, full_matrices=True)
    diago = 1/s
    hp1 = np.dot(np.transpose(V), np.diag(diago))
    hp2 = np.dot(hp1, np.transpose(U))
    h = np.dot(hp2,b)
    
    # Resultado
    H2 = np.array([[h[0,0],h[1,0],h[2,0]],[h[3,0],h[4,0],h[5,0]],[h[6,0],h[7,0],1]])
    return H2
