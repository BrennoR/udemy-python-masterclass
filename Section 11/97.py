# Parabola - More on Functions

try:
    import tkinter
except ImportError:     # python 2
    import Tkinter as tkinter

import math


# def parabola(x):
#     y = x * x / 100
#     return y


def parabola(page, size):
    for x in range(size):
        y = x * x / size
        plot(page, x, y)
        plot(page, -x, y)


# Challenge: modify circle function to include a color parameter for the circle color and default to red when nothing
# is specified


def circle(page, radius, g, h):
    for x in range(g * 100, (g + radius) * 100):
        x /= 100
        print(x)
        y = h + (math.sqrt(radius ** 2 - ((x - g) ** 2)))
        plot(page, x, y)
        plot(page, x, 2 * h - y)
        plot(page, 2 * g - x, y)
        plot(page, 2 * g - x, 2 * h - y)


def circle2(page, radius, g, h, color='red'):
    page.create_oval(g + radius, h + radius, g - radius, h - radius, outline=color, width=2)


def draw_axes(page):
    page.update()         # need to call update to make winfo values available
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill="black")
    page.create_line(0, y_origin, 0, -y_origin, fill="black")
    print(locals())


def plot(page, x, y):
    page.create_line(x, -y, x + 1, -y + 1, fill="red")


mainWindow = tkinter.Tk()

mainWindow.title("Parabola")
mainWindow.geometry('640x480')

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

# canvas2 = tkinter.Canvas(mainWindow, width=320, height=480, background='blue')
# canvas2.grid(row=0, column=1)

# print(repr(canvas), repr(canvas2))
draw_axes(canvas)
# draw_axes(canvas2)

# for x in range(-300, 301):
#     y = parabola(x)
#     plot(canvas, x, -y)     # canvas has y values increasing downward, opposed to traditional methods

parabola(canvas, 100)
parabola(canvas, 200)
# circle(canvas, 100, 100, 100)
# circle(canvas, 100, -100, 100)
# circle(canvas, 100, -100, -100)
# circle(canvas, 50, 10, -20)
circle2(canvas, 10, 10, 10, 'blue')
circle2(canvas, 50, -10, 10, 'green')
circle2(canvas, 100, -100, -100)
circle2(canvas, 50, 10, -20, 'yellow')
circle2(canvas, 120, -15, 20, 'black')

mainWindow.mainloop()

# class functions are called methods
