class AlphaBeta:

    def __init__(self,game):
        self.game = game 
        
    def max_value(self, state, alpha, beta,player,prof):
        if self.game.terminal_test(state):
            return self.game.utility(state, player)
        player = self.game.to_move(state)    
        v = -float("inf")
        for a in self.game.actions(state):
            v = max(v, self.min_value(self.game.result(state, a), alpha, beta,player,prof-1))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(self, state, alpha, beta,player,prof):
        if prof==1 or self.game.terminal_test(state):
            return self.game.utility(state, player)
        v = float("inf")
        for a in self.game.actions(state):
            v = min(v, self.max_value(self.game.result(state, a), alpha, beta,player,prof-1))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v
    
    def run (self,state,prof):
        #print('Alpha beta corriendo')
        #print(self.game.actions(state))
        player = self.game.to_move(state)
        best_score = -float("inf")
        beta = float("inf")
        best_action = None
        #print('actions ')
        for a in self.game.actions(state):
            #print('alpha')
            #print(prof)
            #print(a)
            v = self.min_value(self.game.result(state, a), best_score, beta, player,prof)
            if v > best_score:
                best_score = v
                best_action = a
        print(best_action)
        return best_action
    

    







