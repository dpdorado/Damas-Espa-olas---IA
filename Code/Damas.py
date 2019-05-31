from AlphaBeta import AlphaBeta
from Game import Game

class Damas(Game):

    def __init__(self,view):
        super().__init__(view)
        self.winner=False
        self.level=8
        self.state=self.state._replace(to_move=1)
        self.state=self.state._replace(board=self.init_state())
        self.View.update(self.state.board)

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
                    list_aux.append(1)
                    continue
                if i>4 and (j+i)%2!=0:
                    list_aux.append(2)
                    continue
                list_aux.append(0)
            list.append(list_aux)
        return list

    def actions(self, state):
        #retorna[i,j] son las pociicones
        moves=[]
        #player=state.to_move
        posY=0
        if(len(state)==4):
            if(player==2):
                if (state[0])[state[2][0]][state[2][1]] == 4:
                    fichasAsesinadas=self.matarReina(state[0],state[2],player+2)
                    if len(fichasAsesinadas) > 0:
                        for ficha in fichasAsesinadas:
                            move=self.movFichaAsesinada(ficha,state[0])
                            moves.append(move)
                else:
                    ficha = self.puedeMatar(state[0],state[2][0], state[2][1], [1,3], 1, -1) #-1: por diagonal Derecha
                    if len(ficha) > 0:                
                        moves.append(self.movFichaAsesinada(ficha,state[0]))
                    ficha = self.puedeMatar(state[0],state[2][0], state[2][1], [1,3], 1, 1) #-1: por diagonal Derecha
                    if len(ficha) > 0:           
                        moves.append(self.movFichaAsesinada(ficha,state[0]))
            else:
                ficha = self.puedeMatar(state[0],state[2][0], state[2][1], [2,4], -1, -1) #-1: por diagonal Derecha
                if len(ficha) > 0:                   
                    moves.append(self.movFichaAsesinada(ficha,state[0]))
                ficha = self.puedeMatar(state[0],state[2][0], state[2][1], [2,4], -1, 1) #-1: por diagonal Derecha
                if len(ficha) > 0:  
                    moves.append(self.movFichaAsesinada(ficha,state[0]))            
        else: 
            fichasAsesinadas=self.fichasQuePuedenMatar(player, state[0])
            if(len(fichasAsesinadas)>0):
                for ficha in fichasAsesinadas:
                    move=self.movFichaAsesinada(ficha,state[0])
                    moves.append(move)
            else:      
                for y in state[0]:
                    posX=0
                    for x in y:
                        if(player==2):
                            if(x==2 or x==4):
                                if x==4:
                                    movesReina=self.movReina(state[0],[posY,posX])
                                    for move in movesReina:
                                        moves.append(move)
                                else:
                                    move=self.moverAbajoIzq(state[0],[posY,posX])
                                    if move != None:
                                         moves.append(move)
                                    move=self.moverAbajoDer(state[0],[posY,posX])
                                    if move != None:
                                         moves.append(move)
                        else:    
                            if(x==1 or x==3):
                                if x==3:
                                    movesReina=self.movReina(state[0],[posY,posX])
                                    for move in movesReina:
                                        moves.append(move)
                                else:
                                    move=self.moverArribaIzq(state[0],[posY,posX])
                                    if move != None:
                                         moves.append(move)
                                    move=self.moverArribaDer(state[0],[posY,posX])
                                    if move != None:
                                        moves.append(move)
                        posX=posX+1
                    posY=posY+1  
        return moves


    def result(self, state, move):
        """Return the state that results from making a move from a state."""
        board_r=state.board
        board_r[move[0]][move[1]]=state.to_move
        state=state._raplace(board=board_r)
        return state
    
    def utility(self, state, player):
        """Return the value of this final state to player."""
        pass
    
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
        """run game"""
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
        self.play_game(pos)

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
    def move_machine(self):
        #TODO
        state=self.state
        machine=AlphaBeta(self)
        move = machine.run(state,self.level)
        state = self.result(state,move)
        self.state=self.state._replace(to_move=1)
        return state.board

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

  
        