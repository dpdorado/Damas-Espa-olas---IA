from collections import namedtuple
from abc import ABC, abstractmethod
from AlphaBeta import AlphaBeta


class Game(ABC):
    """A game is similar to a problem, but it has a utility for each
    state and a terminal test instead of a path cost and a goal
    test. To create a game, subclass this class and implement actions,
    result, utility, and terminal_test. You may override display and
    successors or you can inherit their default methods. You will also
    need to set the .initial attribute to the initial state; this can
    be done in the constructor."""
    

    def __init__(self,view):
        GameState = namedtuple('GameState', 'to_move, utility, board, moves')
        self.moves=[]
        self.state = GameState(to_move='', utility=0, board=[], moves=self.moves)
        self.View=view
        self.machine= AlphaBeta(self)

    @abstractmethod
    def init_state(self):
        pass
    
    @abstractmethod
    def actions(self, state):
        """Return a list of the allowable moves at this point."""
        pass

    @abstractmethod
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

    @abstractmethod
    def play_game(self,pos=None):
        """run game"""
        pass
    
    @abstractmethod
    def update(self,list):
        pass

    @abstractmethod
    def move_machine(self,model,player,prof):
        pass

