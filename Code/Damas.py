from Game import Game
from AlphaBeta import AlphaBeta

class Damas(Game):

    def __init__(self):
        super().__init__()
    
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
        pass
    
    @abstractmethod
    def utility(self, state, player):
        """Return the value of this final state to player."""
        pass
    
    @abstractmethod
    def terminal_test(self, state):
        """Return True if this is a final state for the game."""
        pass

    def to_move(self, state):
        """Return the player whose move it is in this state."""
        return state.to_move

    def display(self, state):
        """Print or otherwise display the state."""
        print(state)

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    def play_game(self):
        """run game"""
        pass

    '''Métodos auxiales'''