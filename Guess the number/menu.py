from tkinter import *

def game():
    ws.destroy()
    import app

def instr():
    ws.destroy()
    import instruction

def change_setting():
    ws.destroy()
    import chng_setting


ws = Tk()
ws.title('PythonGuides')
ws.geometry('600x500')
ws.config(bg='#0D0D0D')

start_game = Button(
    ws,
    width=20,
    text='Start Game',
    font=('sans-serif', 14),
    bg='#8C3232',
    fg='white',
    command= game
)
start_game.place(x=160, y=120)

instructions = Button(
    ws,
    width=20,
    text='Instructions',
    font=('sans-serif', 14),
    bg='#8C3232',
    fg='white',
    command=instr
)
instructions.place(x=160, y=170)


setting = Button(
    ws,
    width=20,
    text='Settings',
    font=('sans-serif', 14),
    bg='#8C3232',
    fg='white',
    command=change_setting
)
setting.place(x=160, y=220)


exit = Button(
    ws,
    width=20,
    text='Quit Game',
    font=('sans-serif', 14),
    bg='#8C3232',
    fg='white',
    command=exit
)
exit.place(x=160, y=270)


ws.mainloop()