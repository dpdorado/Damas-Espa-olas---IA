from Board import App
from tkinter import Tk
from Damas import Damas
from ControllerDamas import ControllerDamas



if __name__=="__main__":
    #print(init_state())
    root = Tk()
    app = App(root)
    game = Damas(app)
    controller= ControllerDamas(app,game)
    app.set_controller(controller)
    root.mainloop()
