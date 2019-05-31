# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 09:31:26 2018

@author: eumartinez

"""
from Controller import Controller

class ControllerDamas(Controller):
    def __init__(self,view,model):
        super().__init__(view,model)

    def update(self,pos):
        #Recibir la lista del tablero y la envía al game
        self.Model.update(pos)
   

