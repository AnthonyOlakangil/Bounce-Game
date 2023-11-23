from tkinter import *
import random
import time
import sys

tk = Tk()
tk2 = Tk()
tk2.title('MENU')
canvas2 = Canvas(tk2, width = 100, height = 5)
tk.title('Bounce Game')
tk2.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width = 500, height = 400, bd = 0, highlightthickness = 0)
backgrounds = ['black', 'green', 'purple', 'yellow']
canvas.configure(bg = random.choice(backgrounds))
canvas2.pack()
canvas.pack()
tk.update()
tk2.update()


class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10,10,25,25, fill = color)
        self.canvas.move(self.id, 235, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.score = 0
        self.canvas.create_rectangle(365,0,490,30, fill = 'white')
        self.text = self.canvas.create_text(420, 20, text = 'SCORE: %s' % self.score, font = ('Courier', 15))

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                return True
        return False

    def Score(self):
        pos = self.canvas.coords(self.id)
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                self.score = self.score+1
                self.canvas.itemconfig(self.text, text = 'SCORE: %s' % self.score)
                self.canvas.update()

    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] > self.canvas_height:
            self.canvas.destroy()
            canvas = Canvas(tk, width = 500, height = 400, bd=5, highlightthickness = 10)
            canvas.pack()
            canvas.create_text(250, 250, text = 'GAME OVER', font = ('Courier', 30))
            text2 = canvas.create_text(280, 280, text = 'YOUR SCORE: %s' % self.score, font = ('Courier', 15), fill = 'blue')
            tk2.destroy()
                        
        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3



class Paddle:
    def init(self, canvas, color):
        canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill = color)
        canvas.move(self.id, 200,300)
        self.x = 0
            
    def draw(self):
        canvas_width = canvas.winfo_width()
        canvas.move(self.id, self.x, 0)
        pos = canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= canvas_width:
            self.x = 0
    def arrowkey_binds(self):    
        canvas.bind_all('<KeyPress-Left>', self.turn_left)
        canvas.bind_all('<KeyPress-Right>', self.turn_right)
        
    def turn_left(self, event):
        self.x = -5

    def turn_right(self, event):
        self.x = 5

    def mouse_keybinds(self):
        canvas.bind_all('<Motion>', self.move_mouse)

    def move_mouse(self, event):
        pos = canvas.coords(self.id)
        middle_of_paddle = (pos[0] + pos[2]) / 2
        move = event.x - middle_of_paddle
        self.x = move
        
    def menu(self):
        btn = Button(tk2, text = 'mouse', command=self.mouse_keybinds)
        btn2 = Button(tk2, text = 'arrow keys', command=self.arrowkey_binds)
        btn.pack()
        btn2.pack()
        
        
paddle = Paddle() 
paddle.init(canvas, 'blue')
ball = Ball(canvas, paddle,'red')
paddle.menu()

def updater():
    while 1:
        ball.draw()
        paddle.draw()
        ball.Score()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.001)
        

start_button =  Button(tk, text = 'START',command=updater)
start_button.pack()


tk.mainloop()
