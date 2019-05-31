# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 09:31:26 2018

@author: eumartinez

"""

class Controller:
    def __init__(self,view,model):
        self.View=view
        self.Model=model
        super().__init__()

    def update(self,pos=[]):
        pass
   

