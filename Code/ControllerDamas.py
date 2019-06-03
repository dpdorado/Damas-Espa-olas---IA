# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 09:31:26 2018

@author: eumartinez

"""
from Controller import Controller
from collections import namedtuple
import time

class ControllerDamas(Controller):
    def __init__(self,view,model):
        #GameState = namedtuple('GameState', 'to_move, utility, board, moves')
        self.can_move=False
        self.chips_can_kill=[]
        self.for_kill=[]
        self.select=[]
        self.played=False
        self.new_model=view.get_model()
        self.prof=4
        super().__init__(view,model)

    def obligate_check_chip(self,pos):
        result=False
        for i in range(len(self.chips_can_kill)):
            list=self.chips_can_kill[i][0]
            if list[0] == pos[0] and list[1] == pos[1]:
                tupla=(self.chips_can_kill[i][1], self.chips_can_kill[i][2])
                self.for_kill.append(tupla)
                result=True
        return result
    
    def check_move(self, pos):          
        for i in range(len(self.for_kill)):
            if pos[0] == self.for_kill[i][1][0] and pos[1] == self.for_kill[i][1][1]:
                model=self.View.get_model()
                self.View.change_pos(pos,model[self.select[0]][self.select[1]],self.select)  
                self.View.remove_pos([self.for_kill[i][0][0], self.for_kill[i][0][1]])
                return True
        return False
                
    #
    def do_changes(self,pos):
        model=self.View.get_model()
        if self.can_move:
            if model[pos[0]][pos[1]] == 0 and len(self.chips_can_kill) > 0:
                if (self.check_move(pos)):
                        self.chips_can_kill=self.Model.chips_can_kill(self.View.get_player(),model)
                        if not (len(self.chips_can_kill) > 0):
                            self.View.update()
                            self.View.set_player(2)
            elif pos[0] == self.select[0]-1:  
                if pos[1] == self.select[1]-1:
                    self.can_move=self.View.change_pos(pos,model[self.select[0]][self.select[1]],self.select)
                    self.View.set_player(2)
                if pos[1] == self.select[1]+1:
                    self.can_move=self.View.change_pos(pos,model[self.select[0]][self.select[1]],self.select) 
                    self.View.set_player(2)              
        player=self.View.get_player()
        if (player==1):
            print('player 1')
            if model[pos[0]][pos[1]] in [1,3]:
                print('player 1.1')
                self.chips_can_kill=self.Model.chips_can_kill(player, model)
                print(self.chips_can_kill)
                if len(self.chips_can_kill) > 0:
                    if (self.obligate_check_chip(pos)):
                        print('abkigando')
                        self.select=pos
                        self.can_move=True
                else:
                    print('player 1.2')
                    self.select=pos
                    self.can_move=True
        else:
            print('maquina')
            if(self.played==False):
                self.new_model=self.View.get_model()
            self.new_model=self.Model.move_machine(self.new_model,self.View.get_player(),self.prof)

            if(self.new_model!=None):
                self.select=self.new_model[1]
                
                self.View.change_pos([self.new_model[2][0],self.new_model[2][1]],(self.new_model[0])[self.new_model[2][0]][self.new_model[2][1]],self.select)
                for z in self.new_model[0]:
                    print(z)
                print(self.select)
                if(len(self.new_model)>3):
                        self.View.remove_pos([self.new_model[3][0],self.new_model[3][1]])
                        self.played=True
                else :
                    self.View.set_player(1)
                    self.played=False
                    for i in self.View.get_model():
                        print(i)
                self.View.update()
            else:
                self.View.set_player(1)
                self.played=False
                for i in self.View.get_model():
                        print(i)
                self.View.update()


    def update(self,pos):
        #Recibir la lista del tablero y la envía al game
        self.do_changes(pos)
        #self.Model.update(pos)
   

