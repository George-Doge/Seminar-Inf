'''
# I have commented this out, bcs it is not good to run it. If you happen to run it, then stop it with Ctrl+C in console
import tkinter

window = tkinter.Tk()
canvas = tkinter.Canvas(width=800, height=200, bg="blue")
canvas.pack()


def cloud():
    x, y = 75, 100
    r = 40

    canvas.create_oval(x-r-30, y-r, x+r+30, y+r, fill="white", tags="mrak")


def sun():
    x, y = 750, 100
    r = 50
    canvas.create_oval(x-r, y-r, x+r, y+r, fill="yellow")


def move(coord):
        x_counter = 75
        for i in range(63):
            canvas.move('mrak', 10, 0)
            x_counter += 10
            canvas.after(20)
            canvas.update()

        while x_counter >= 600:
            cloud()


sun()
cloud()
while True:
    canvas.bind("<Button-1>", move)
    canvas.update()

window.mainloop()
'''