from tkinter import *
from cell import Cell
import settings
import utils 


# Window Settings
root = Tk()
root.configure(bg="black") #Assigns a color to the background. You can also use hexa-decimals here
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Py_sweeper")
root.resizable(False, False) # Disables the resizing of the window, including Full Screen.

# The 3 Main Frames 
top_frame= Frame(
    root,
    bg='red',
    width=settings.WIDTH,
    height=utils.height_prct(25) 
    )
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='blue',
    width=utils.width_prct(25),
    height=utils.height_prct(75) 
    )

left_frame.place(x=0, y=utils.height_prct(25))

center_frame= Frame(
    root,
    bg='green',
    width=utils.width_prct(75),
    height=utils.height_prct(75) 
    )
center_frame.place(x=utils.width_prct(25), y=utils.height_prct(25))

# Single Cells Instantiation
"""
c1 = Cell()
c1.create_btn_object(center_frame)
c1.cell_btn_object.grid(column=0,row=0) 

c2 = Cell()
c2.create_btn_object(center_frame)
c2.cell_btn_object.grid(column=1,row=1) 
"""

# Multiple Cells Instantiation
for x in range(settings.GRID_SIZE):
    for y in range (settings.GRID_SIZE):
        c = Cell(x,y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(column=x,row=y) 


Cell.randomize_mines()

# Run the game
root.mainloop()