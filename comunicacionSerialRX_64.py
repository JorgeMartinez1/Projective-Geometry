#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Insert module description here

Created on Wed Sep 13 18:07:14 2017
@author: gholguin
"""

# Imports


# +=================================================================================================
class Miclase():
    """Class Description here"""

    # Define class attributes
    a_int = 0
    a_list = list()

    # ----------------------------------------------------------------------------------------------
    def __init__(self, arg1, arg2):
        """Constructor"""

        # Define object attributes
        self.altura = arg1
        self.lista = list()

        # contructor code here

    # ----------------------------------------------------------------------------------------------
    def mymethod(self, arg1, arg2):
        'A method to do some stuff with the attributes of the class'

        # do some stuff here
        print(arg1, arg2, self.a_int)

        return

    # ----------------------------------------------------------------------------------------------
    @staticmethod
    def mifuncionestatica(arg1):
        'An example of a function that does not require the object'

        # do some stuff here
        print(arg1)

        return arg1+1

# +=================================================================================================
def main():
    'A main function, basically to test the class or classes'

    # Do some stuff here
    miobjeto = Miclase(1, 2)

    a = miobjeto.altura
    miobjeto.mymethod(1, 2)


    miobjeto.mymethod(3, 4)


    mi_otro_objeto = Miclase(255, 139)
    b = mi_otro_objeto.altura

    return

# +=================================================================================================
if __name__ == "__main__":
    main()

