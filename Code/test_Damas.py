from Board import App
from tkinter import Tk
from Game import Game
from Controller import Controller



if __name__=="__main__":
    #print(init_state())
    root = Tk()
    app = App(root)
    game = Game(app)
    controller= Controller(app,game)
    app.set_controller(controller)
    root.mainloop()
