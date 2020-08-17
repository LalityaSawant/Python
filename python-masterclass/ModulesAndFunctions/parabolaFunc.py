# import turtle
# import random
import tkinter
# import math


def parabola(page, size):
    for x in range(size):
        y = (x * x) / size
        plot(page, x, y)
        plot(page, -x, y)


def circle(page, radius, g, h, color='red'):
    page.create_oval(g + radius, h + radius, g - radius, h - radius, outline=color, width=2)
    # for x in range(g * 10, (g + radius) * 10):
    #     x /= 10
    #     y = h + (math.sqrt(radius ** 2 - ((x-g) ** 2)))
    #     plot(page, x, y)
    #     plot(page, x, 2 * h - y)
    #     plot(page, 2 * g - x, y)
    #     plot(page, 2 * g - x, 2 * h - y)


def draw_axis(page):
    canvas.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill='black')
    page.create_line(0, y_origin, 0, -y_origin, fill='black')


def plot(page, x, y):
    page.create_line(x, -y, x+1, -y+1, fill='red')


mainWindow = tkinter.Tk()

mainWindow.title('Parabola')
mainWindow.geometry("640x480")

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

draw_axis(canvas)

# for x in range(-100, 100):
#     y = parabola(x)
#     #print(x, y, sep=':')
#     plot(canvas, x, -y)

parabola(canvas, 100)
parabola(canvas, 200)
circle(canvas, 100, 100, 100, 'red')
circle(canvas, 100, 100, -100, 'green')
circle(canvas, 100, -100, 100, 'blue')
circle(canvas, 100, -100, -100, 'yellow')
circle(canvas, 10, 30, 30, 'purple')
circle(canvas, 10, 30, -30, 'orange')
circle(canvas, 10, -30, 30, 'olive')
circle(canvas, 10, -30, -30, 'violet')
circle(canvas, 30, 0, 0)

mainWindow.mainloop()

# def draw_circle(color,size):
#     turtle.color(color)
#     turtle.circle(size)
#
#
# #turtle.speed(500000)
#
# circle_size = .5
#
# for j in range(1,360):
#     turtle.left(3)
#     for i in range(1,360):
#         turtle.forward(i)
#         turtle.left(7)
#         turtle.color()
#         turtle.goto(j,j)
#         turtle.color('black')
#         turtle.forward(10)
#
#
# # for j in range(1,50):
# #     #turtle.color('white')
# #     turtle.left(10)
# #     turtle.forward(10)
# #     color_selected = 'black' #random.choice(['red','blue','green','purple'])
# #     for i in range(1,10):
# #         #turtle.color('white')
# #         turtle.right(20)
# #         #turtle.forward(10)
# #         for x in range(0,10):
# #             y = parabola(x)
# #             #circle_size += j
# #             print(j,i,x,y,circle_size, sep=':')
# #             #turtle.color('white')
# #             #turtle.goto(x,y)
# #             turtle.right(30)
# #             #turtle.forward(10)
# #            # turtle.forward(x-10)
# #            # draw_circle(color_selected,circle_size)
# #             #turtle.color('black')
#
#
# turtle.done()
