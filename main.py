from tkinter import *

import configure
import new

root = Tk()
root.configure(bg = "black")
root.geometry(f'{configure.WIDTH}x{configure.HEIGHT}')
root.title("Minesweeper")
root.resizable(False,False )

top_frame = Frame(root,bg="grey",width=configure.WIDTH,
                  height=new.height_prct(25))
top_frame.place(x=10,y=10 )
root.mainloop()