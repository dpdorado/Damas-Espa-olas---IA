from AlphaBeta import AlphaBeta
from Game import Game
from copy import copy

class Damas(Game):
    def __init__(self,view):
        super().__init__(view)
        self.LEFT=-1
        self.RIGHT=1
        self.DOWN=1
        self.UP=-1
        self.state=self.state._replace(to_move=1)
        self.state=self.state._replace(board=self.init_state())
        self.View.update([self.state.board])

    #Inicia el tablero por defecto -> inicio del juego.
    def init_state(self):
        list=[]
        for i in range(8):
            list_aux=[]
            for j in range(8):
                if i in [3,4]:
                    list_aux.append(0)
                    continue
                if i<3 and (j+i)%2!=0:
                    list_aux.append(2)
                    continue
                if i>4 and (j+i)%2!=0:
                    list_aux.append(1)
                    continue
                list_aux.append(0)
            list.append(list_aux)
        return list

    def actions(self, state):
        #retorna[i,j] son las posiciones
        moves=[]
        n_state=copy(state)
        #print('n_state')
        #print(n_state)
        player=n_state.to_move
        moves_current=n_state.moves
        board=n_state.board

        posY=0
        if(len(moves_current)==3):
            #print('==3')
            if(player==2):
                #print('==2')
                if board[moves_current[2][0]][moves_current[2][1]] == 4:
                    chips_deed=self.queen_kill(board, moves_current[1],player+2)
                    if len(chips_deed) > 0:
                        #realizar movimiento???
                        for chip in chips_deed:
                            move=self.move_chip_deed(chip,n_state)
                            moves.append(move)
                else:
                    #print('else ==11111')
                    chips_m = self.can_kill(board,moves_current[2], [1,3], self.DOWN, self.LEFT)
                    #hacer movimiento
                    if len(chips_m) > 0:                
                        moves.append(self.move_chip_deed(chips_m,n_state))
                    chips_m = self.can_kill(board,moves_current[2], [1,3], self.DOWN, self.RIGHT)
                    #hacer movimiento
                    if len(chips_m) > 0:           
                         moves.append(self.move_chip_deed(chips_m,n_state))
            else:
                #print('else ==2')
                chips_m = self.can_kill(board,moves_current[2], [2,4], self.UP, self.LEFT)
                if len(chips_m) > 0:  
                    #hacer movimiento
                    moves.append(self.move_chip_deed(chips_m,n_state))
                chips_m = self.can_kill(board,moves_current[2], [2,4], self.UP, self.RIGHT)
                if len(chips_m) > 0:  
                    #hacer movimiento
                    moves.append(self.move_chip_deed(chips_m,n_state))            
        else: 
            #print('else mayor')
            chips_deed=self.chips_can_kill(player, board)
            #print('chips_deed')
            #print(chips_deed)
            if(len(chips_deed)>0):
                #hacer movimiento
                for chip in chips_deed:
                    move=self.move_chip_deed(chip,n_state)
                    moves.append(move)
            else:    
                #print('for')  
                for y in board:
                    posX=0
                    for x in y:
                        if(player==2):
                            if(x==2 or x==4):
                                if x==4:
                                    moves_queen=self.move_queen(board,[posY,posX])
                                    #print('moves_queen')
                                    #print(moves_queen)
                                    for move in moves_queen:
                                        moves.append(move)
                                else:
                                    move=self.move_down_left(board,[posY,posX])
                                    #print('left')
                                    #print(move)
                                    if move != None:
                                        moves.append(move)
                                    move=self.move_down_left(board,[posY,posX])
                                    #print('right')
                                    #print(move)
                                    if move != None:
                                        moves.append(move)
                        else:    
                            if(x==1 or x==3):
                                if x==3:
                                    moves_queen=self.move_queen(board,[posY,posX])
                                    #print('moves_queen else')
                                    #print(moves_queen)
                                    for move in moves_queen:
                                        moves.append(move)
                                else:
                                    move=self.move_up_left(board,[posY,posX])
                                    #print('left_')
                                    #print(move)
                                    if move != None:
                                         moves.append(move)
                                    #print('right_')
                                    #print(move)
                                    move=self.move_up_right(board,[posY,posX])
                                    if move != None:
                                        moves.append(move)
                        posX=posX+1
                    posY=posY+1
        #print('moves')
        #print(moves) 
        return moves
    
    def move_chip_deed(self,chip,state):
        ###--------------------
        n_state=copy(state)
        board=n_state.board

        board[chip[2][0]][chip[2][1]]= board[chip[0][0]][chip[0][1]]
        board[chip[0][0]][chip[0][1]]=0
        board[chip[1][0]][chip[1][1]]=0

        move=(board,chip[0],chip[2],chip[1])
        return move
    #
    def move_down_left(self,model,pos):
        board=None
        if pos[0]<7 and pos[1]>0:
            if model[pos[0]+1][pos[1]-1]==0:
                new_model=[x[:] for x in model]
                if pos[0]==6 and new_model[pos[0]][pos[1]]==2 :
                    new_model[pos[0]+1][pos[1]-1]=4
                else:    
                    new_model[pos[0]+1][pos[1]-1]=new_model[pos[0]][pos[1]]
                new_model[pos[0]][pos[1]]=0
                board=[new_model,pos,(pos[0]+1,pos[1]-1)]
        return board
        
    def move_down_right(self,model,pos):
        board=None
        if pos[0]<7 and pos[1]<7:
             if model[pos[0]+1][pos[1]+1]==0:
                new_model=[x[:] for x in model] 
                if pos[0]==6 and new_model[pos[0]][pos[1]] == 2:
                    new_model[pos[0]+1][pos[1]+1]=4
                else:
                    new_model[pos[0]+1][pos[1]+1]=new_model[pos[0]][pos[1]]
                new_model[pos[0]][pos[1]]=0
                board=[new_model,pos,(pos[0]+1,pos[1]+1)]
        return board
    def move_up_left(self,model,pos):
        board=None
        if pos[0]>0 and pos[1]>0:
            if model[pos[0]-1][pos[1]-1]==0:
                new_model=[x[:] for x in model]
                if pos[0]==1 and new_model[pos[0]][pos[1]] ==1:
                    new_model[pos[0]-1][pos[1]-1]=3
                else:
                    new_model[pos[0]-1][pos[1]-1]=new_model[pos[0]][pos[1]]
                new_model[pos[0]][pos[1]]=0
                board=[new_model,pos,(pos[0]-1,pos[1]-1)]
        return board
    def move_up_right(self,model,pos):
        board=None
        if pos[0]>0 and pos[1]<7:
            if model[pos[0]-1][pos[1]+1]==0:
                new_model=[x[:] for x in model]
                if pos[0]==1 and new_model[pos[0]][pos[1]]==1:
                    new_model[pos[0]-1][pos[1]+1]=3
                else:
                    new_model[pos[0]-1][pos[1]+1]=new_model[pos[0]][pos[1]]
                new_model[pos[0]][pos[1]]=0
                board=[new_model,pos,(pos[0]-1,pos[1]+1)]
        return board
    def move_queen(self,model,pos):
        move_chips_queen=[]
        pos_aux=[pos[0],pos[1]]
        model_aux=[x[:] for x in model] 

        while(pos_aux[0]>0 and pos_aux[1] > 0):
            #matar diagonalIzq
            move=self.move_up_left(model_aux,pos_aux)
            if(move!=None):
               move[1]=pos
               move_chips_queen.append(move)
               model_aux=move[0]
            pos_aux[0]=pos_aux[0]-1
            pos_aux[1]=pos_aux[1]-1
        model_aux=[x[:] for x in model]
        pos_aux=[pos[0],pos[1]]   
        while(pos_aux[0]>0 and pos_aux[1] < 7):
            #matar diagonalDer
            move=self.move_up_right(model_aux,pos_aux)
            if(move!=None):
               move[1]=pos
               move_chips_queen.append(move)
               model_aux=move[0]
            pos_aux[0]=pos_aux[0]-1
            pos_aux[1]=pos_aux[1]+1
        model_aux=[x[:] for x in model]
        pos_aux=[pos[0],pos[1]]
        while(pos_aux[0]<7 and pos_aux[1] > 0):
            #matar diagonalAbajIzq
            move=self.move_down_left(model_aux,pos_aux)
            if(move!=None):
               move[1]=pos
               move_chips_queen.append(move)
               model_aux=move[0]
            pos_aux[0]=pos_aux[0]+1
            pos_aux[1]=pos_aux[1]-1
        model_aux=[x[:] for x in model]
        pos_aux=[pos[0],pos[1]]
        while(pos_aux[0]<7 and pos_aux[1] < 7):
            #matar diagonalAbajoDer
            move=self.move_down_right(model_aux,pos_aux)
            if(move!=None):
               move[1]=pos
               move_chips_queen.append(move)
               model_aux=move[0]
            pos_aux[0]=pos_aux[0]+1
            pos_aux[1]=pos_aux[1]+1
        #retorna la board + moves???
        return move_chips_queen  


    def result(self, state, move):
        """Return the state that results from making a move from a state."""
        #la lógica esta regular, los movimiento se estan aplicando en actions, colocar algo adicional en las acciones para saber que mover,dama o peon
        #print('result')
        state_c=copy(state)
        #print('result')
        state_c=state._replace(board=move[0])
        #print('result')
        moves=[]
        moves.append(move[1])
        moves.append(move[2])
        #print('result')
        if len(move)==3:
            moves.append(move[2])
        #print('result')
        state_c=state_c._replace(moves=moves)
        player=1 if state_c.to_move==2 else 2
        state_c=state_c._replace(to_move=player)
        #print(state_c)
        return state_c

    def fichasAlrededor(self,tablero,posFicha,player):
        nFichasProtec=0
        if posFicha[0]<7 and posFicha[1]>0:
            if tablero[posFicha[0]+1][posFicha[1]-1]==player or tablero[posFicha[0]+1][posFicha[1]-1]==player+2:
                 nFichasProtec=nFichasProtec+1
        if posFicha[0]<7 and posFicha[1]<7:
            if tablero[posFicha[0]+1][posFicha[1]+1]==player or tablero[posFicha[0]+1][posFicha[1]+1]==player+2:
                 nFichasProtec=nFichasProtec+1
        if posFicha[0]>0 and posFicha[1]>0:
            if tablero[posFicha[0]-1][posFicha[1]-1]==player or tablero[posFicha[0]-1][posFicha[1]-1]==player+2:
                 nFichasProtec=nFichasProtec+1
        if posFicha[0]>0 and posFicha[1]<7:     
            if tablero[posFicha[0]-1][posFicha[1]+1]==player or tablero[posFicha[0]-1][posFicha[1]+1]==player+2:
                nFichasProtec=nFichasProtec+1
        return nFichasProtec

    def utility(self, state, player):
        #print('utility')
        print(state)
        board=state.board
        nFichasMaquina = 0
        nFichasJugador = 0
        nFichasProtecM=0
        nFichasProtecJ=0
        posY = 0
        for y in board:
            #print('row')
            #print(y)
            posX=0
            for x in y:
                #print('check')
                #print(x)
                if x==2 or x==4:
                    nFichasMaquina+=  nFichasMaquina
                    nFichasProtecM=nFichasProtecM+self.fichasAlrededor(board,[posY,posX],2)
                if x==1 or x==3:
                    nFichasJugador+= nFichasJugador
                    nFichasProtecJ=nFichasProtecJ+self.fichasAlrededor(board,[posY,posX],1)
                posX=posX+1
            posY=posY+1
        """Se calcula dandole mas valor al multiplicador del numero de reinas de la maquina y del jugador
        para calcular la diferencia entre el primero y el segundo mas la misma operación con los peones
        dandole un valor de 5 multiplicador mas 2 * la cantidad de fichascustodiadas de la maquina 
        menos la cantidad de fichas custodiadas de la maquina"""
        """10 * nFichasReinasM - 10* nFichasReinasJ +""" 
        utility =  5*nFichasMaquina  - 5*nFichasJugador +  2 * nFichasProtecM - nFichasProtecJ
        #print('utility')
        #print(utility)
        return utility
    
    def terminal_test(self, state):
        """Return True if this is a final state for the game."""
        if self.count_chips_machine() == 0 or self.count_chips_user() == 0:
            return True
        return False

    def to_move(self, state):
        """Return the player whose move it is in this state."""
        return state.to_move

    def display(self, state):
        """Print or otherwise display the state."""
        #NO ES NECESARIO
        print(state)

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)
    
    def play_game(self,pos):
        
        mov_user=[]
        mov_machine=[]

        #NO SE UTLIZARARÄ
        if self.terminal_test(self.state):
            return [mov_user,mov_machine]

        mov_user=self.move_user(pos)
        if not self.winner:
            mov_machine=self.move_machine()
            if self.winner:
                mov_user=[]
        self.View.update([mov_user,mov_machine])       
       
    def update(self,pos):
        print(pos)
        #self.play_game(pos)
    
    #Movimiento del usuario, retorna el movimiento ya hecho
    def move_user(self,pos):
        move_board=[]
        flag=False
        aux_moves=self.actions(self.state)

        for a in aux_moves:
            if a == pos:
                flag=True
                break
        if flag:
            state=self.result(self.state,pos)
            move_board=state.board
            self.state=self.state._replace(to_move=2)
        return move_board

    #Movimiento de la maquina, retorna el movimiento ya hecho
    """def move_machine(self):
        #TODO
        state=self.state
        machine=AlphaBeta(self)
        move = machine.run(state,self.level)
        state = self.result(state,move)
        self.state=self.state._replace(to_move=1)
        return state.board
    """
    #Cuenta el numero de fichas que tiene la maquina.
    def count_chips_machine(self):
        count=0
        board=self.state.board
        #Buscar solución con expresiones matemáticas
        for row in board:
            for item in row:
                count= count+1 if item==2 else count    
        return count

    #Cuenta el numero de fichas que tiene el jugador.
    def count_chips_user(self):
        count=0
        board=self.state.board
        #Buscar solución con expresiones matemáticas
        for row in board:
            for item in row:
                count= count+1 if item==1 else count    
        return count

    def get_tipo_ficha(self,tipoFicha):
        reina = 1
        peon = 0
        if tipoFicha == 1:
            return reina
        else:
            return peon

    #Métodos utilizados

    #Devuelve todas las posiles muertes que se puedan realizar.
    def chips_can_kill(self, player, model):
        list=[]
        if player == 1:
            opponents = [2,4]
            address = self.UP
        else:
            opponents = [1,3]
            address = self.DOWN     

        for i in range(len(model)):
            row=model[i]
            for j in range(len(row)):
                if model[i][j] == player:
                    #Cuando es un Peon
                    tupla = self.can_kill(model,[i,j], opponents, address, self.LEFT) 
                    if len(tupla) > 0:
                        list.append(tupla)
                    tupla = self.can_kill(model,[i,j], opponents, address, self.RIGHT) 
                    if len(tupla) > 0:
                        list.append(tupla)
                elif model[i][j] == player+2:
                    #Cuado es una Dama
                    tupla=self.queen_kill(model,[i,j],player+2)
                    if len(tupla) > 0:
                        list=self.add_list(list,tupla)
        return list

    #Devulve lista de movimientos posibles si se puede matar.
    def check_option_queen(self, model, pos, opponents,addresses,function):
        dead_chips=[]
        pos_aux=pos
        while(function(pos_aux[0],pos_aux[1])):
            dead_chip=self.can_kill(model,pos_aux, opponents,addresses[0], addresses[1])
            if(len(dead_chip)==0):
                break
            dead_chips.append(dead_chip) 
            pos_aux[0]=pos_aux[0]+addresses[0]
            pos_aux[1]=pos_aux[1]+addresses[1]
        return dead_chips

    #Copia en una lista un conjunto de listas
    def add_list(self,list,list_all):
        list_result=list
        for l in list_all:
            list_result.append(l)
        return list_result

    #Devuelve una lsita de [[],(),()] que contiene la posición ficha actual,la ficha a matar y donde quedará.
    def queen_kill(self, model, pos, player):
        dead_chips=[]
        list_aux=[]

        if  player ==4:
            opponents=[1,3]
        else:
            opponents=[2,4]

        list_aux=self.check_option_queen(model, pos, opponents,[self.UP, self.LEFT],(lambda x,y:x>0 and y>0))
        dead_chips=self.add_list(dead_chips,list_aux)
        list_aux=self.check_option_queen(model, pos, opponents,[self.UP, self.RIGHT],(lambda x,y:x>0 and y<7))
        dead_chips=self.add_list(dead_chips,list_aux)
        list_aux=self.check_option_queen(model, pos, opponents,[self.DOWN, self.LEFT],(lambda x,y:x<7 and y>0))
        dead_chips=self.add_list(dead_chips,list_aux)
        list_aux=self.check_option_queen(model, pos, opponents,[self.DOWN, self.RIGHT],(lambda x,y:x<7 and y<7))
        dead_chips=self.add_list(dead_chips,list_aux)
        return dead_chips  
    
    #Devuleve la posición de la ficha actual,la ficha a matar y donde quedará. -> [[],(),()]
    #cambiar nombre a al método?????
    def can_kill(self, model, pos, opponents, address, side):
        list = []
    
        row_1 = pos[0]+1*address
        column_1 = pos[1]+1*side
        
        row_2 = row_1+1*address
        column_2 = column_1+1*side
           
        if self.check_position([row_1,column_1]) and self.check_position([row_2,column_2]):
            if model[row_1][column_1] in opponents and model[row_2][column_2] == 0:
                list = [pos, (row_1, column_1), (row_2, column_2)]
        return list

    # Verifica si una posición es valida en el tablero ->[i,j] 
    def check_position(self,pos):
        range_rc=range(8)
        if pos[0] in range_rc and pos[1] in range_rc:
            return True
        return False

    #Movimiento de la maquina -> AlphaBeta
    def move_machine(self,model,player,prof):
        #print(self.state)
        #print('erroor')
        #print(model)

        if len(model)<=4:
            self.state=self.state._replace(board=model[0])
        else:
            self.state=self.state._replace(board=model)
        #print(self.state)
        self.state=self.state._replace(to_move=player)
        #print(self.state)
        state=copy(self.state)
        #print(state)
        return self.machine.run(state,prof)
        