# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 09:31:26 2018

@author: eumartinez

"""
from tkinter import *
from Controller import Controller
import time

class App:
       
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        self.height=600
        self.width=600
        self.grid_column=8
        self.grid_row=8
        self.canvas = Canvas(self.frame, height=self.height, width=self.width)
        self.cellwidth = int(self.canvas["width"])/self.grid_column
        self.cellheight = int(self.canvas["height"])/self.grid_row
        self.draw_grid()
        self.canvas.pack()
        self.model=[[0 for x in range(self.grid_column)] for y in range(self.grid_row)]
        self.player = 1
        self.pos=(0,0)
        self.controller=None
        '''self.hi_there = Button(self.frame, text="Jugar", command=self.start_Game)
        self.hi_there.pack(side=LEFT)'''
        
    def set_controller(self,controller):
        self.controller=controller
        def handler(event, self=self):
            return self.__onClick(event)
        self.canvas.bind('<Button-1>', handler)
        
    def __onClick(self,event):

        i=int(event.y/self.cellheight)
        j=int(event.x/self.cellwidth)

        #self.pos =(i,j)
        
        self.notify([i,j])
        print(self.model)
        #self.update()

    
    def draw_grid(self):
        for i in range(self.grid_row):
            for j in range(self.grid_column):
                x1 = i * self.cellwidth
                y1 = j * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                if (i+j)%2==0:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="black")
                      
    def drawChip(self):
        x=self.pos[1]*self.cellwidth
        y=self.pos[0]*self.cellheight
        if(self.player ==1):
            self.canvas.create_oval(x,y,x+self.cellwidth,y+self.cellheight, fill='blue')
            self.player=2
        else:
            self.canvas.create_oval(x,y,x+self.cellwidth,y+self.cellheight, fill='red')
            self.player=1
            
    
    def drawChips(self):
        for i in range(len(self.model)):
            row=self.model[i]
            for j in range(len(row)):
                val=self.model[i][j]
                x=j*self.cellwidth
                y=i*self.cellheight
                if(val ==1):
                    #pinta azul
                    self.canvas.create_oval(x,y,x+self.cellwidth,y+self.cellheight, fill='red')
                elif(val ==2):
                    #pinta rojo
                    self.canvas.create_oval(x,y,x+self.cellwidth,y+self.cellheight, fill='blue')
                    
    def update(self,list=None):
        #arreglar, list contiene un movimiento de user  y movimiento machine
        flag=0
        if list[0]!=[] or list[1]!=[]:
            self.player= 2 if self.player==1 else 1    
            flag=0 if list[0]!=[] else 2
            flag=0 if list[1]!=[] else 1
            if flag == 0:  
                self.model=list[0]
                self.drawChips()
                time.sleep(1)#tiempo entre jugada
                self.model=list[1]
                self.drawChips()
            else:
                self.show_winner(flag)

    def show_winner(self,winner):
        if winner==1:
            messagebox.showinfo("Information","Ganaste!!!")
        else:
            messagebox.showinfo("Information","Gano la maquina!!!")      
    def notify(self,pos=[]):
        self.controller.update(pos)
        
    def  start_Game(self):
        print('start game')
    '''Métodos agregasos DD'''

    def get_model(self):
        return self.model

    def set_model(self,list):
        self.model=list
        
        


