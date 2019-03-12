""" Funcion para hacer interpolacion bilineal con 4 vecinos """

import numpy as np

def inter4vecinos(xp,yp,img):
    
    intery1b = ((((int(xp)+1)-(xp))/((int(xp)+1)-int(xp)))*img.item(int(yp), int(xp), 0)) + (((xp-(int(xp)))/((int(xp)+1)-int(xp)))*img.item(int(yp), int(xp)+1, 0))
            
    intery1g = ((((int(xp)+1)-(xp))/((int(xp)+1)-int(xp)))*img.item(int(yp), int(xp), 1)) + (((xp-(int(xp)))/((int(xp)+1)-int(xp)))*img.item(int(yp), int(xp)+1, 1))
            
    intery1r = ((((int(xp)+1)-(xp))/((int(xp)+1)-int(xp)))*img.item(int(yp), int(xp), 2)) + (((xp-(int(xp)))/((int(xp)+1)-int(xp)))*img.item(int(yp), int(xp)+1, 2))
            
            
    intery2b = ((((int(xp)+1)-(xp))/((int(xp)+1)-int(xp)))*img.item(int(yp)+1, int(xp), 0)) + (((xp-(int(xp)))/((int(xp)+1)-int(xp)))*img.item(int(yp)+1, int(xp)+1, 0))
            
    intery2g = ((((int(xp)+1)-(xp))/((int(xp)+1)-int(xp)))*img.item(int(yp)+1, int(xp), 1)) + (((xp-(int(xp)))/((int(xp)+1)-int(xp)))*img.item(int(yp)+1, int(xp)+1, 1))
            
    intery2r = ((((int(xp)+1)-(xp))/((int(xp)+1)-int(xp)))*img.item(int(yp)+1, int(xp), 2)) + (((xp-(int(xp)))/((int(xp)+1)-int(xp)))*img.item(int(yp)+1, int(xp)+1, 2))
            
            
    interxyb = ((((int(yp)+1)-(yp))/((int(yp)+1)-int(yp)))*intery1b) + (((yp-(int(yp)))/((int(yp)+1)-int(yp)))*intery2b)
            
    interxyg = ((((int(yp)+1)-(yp))/((int(yp)+1)-int(yp)))*intery1g) + (((yp-(int(yp)))/((int(yp)+1)-int(yp)))*intery2g)
            
    interxyr = ((((int(yp)+1)-(yp))/((int(yp)+1)-int(yp)))*intery1r) + (((yp-(int(yp)))/((int(yp)+1)-int(yp)))*intery2r)
    
    return (interxyb, interxyg, interxyr)