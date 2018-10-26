import turtle
import random


head = [0]

#score
a = [0]
b = [0]

#food coord
foodcoord = [0,0,0]

#cposition
cpos = []


def home(x,y):
    x = 0
    y = 0
    a[0] = 0
    b[0] = 0
    head[0] = 0
    foodcoord[2] = 0
    cpos[:] = []
    turtle.hideturtle()
    turtle.clear()
    turtle.pu()
    turtle.color("red")
    turtle.goto(0,0)
    turtle.write("Play")
    turtle.title("My Snake Game")
    turtle.onscreenclick(start)
    turtle.mainloop()

def window():
    turtle.clear()
    turtle.pu()
    turtle.speed(0)
    turtle.pensize(20)
    turtle.color("black")
    turtle.goto(-220,220)
    turtle.pd()
    turtle.goto(220,220)
    turtle.goto(220,-220)
    turtle.goto(-220,-220)
    turtle.goto(-220,220)
    turtle.pu()
    turtle.goto(0,0)

def start(x,y):
    turtle.onscreenclick(None)

    window()

    tfood = turtle.Turtle()
    tfood.hideturtle()
    tfood.pu()
    tfood.speed(0)
    tfood.shape("square")
    tfood.color("red")

    tscore = turtle.Turtle()
    tscore.hideturtle()
    tscore.pu()
    tscore.speed(0)
    tscore.goto(100,-250)
    tscore.write("Score:" + str(a[0]), align="center",font=(10))
    
    while x > -210 and x < 210 and y > -210 and y <210:
        if foodcoord[2] == 0:
            food(tfood)
            foodcoord[2] = 1
        turtle.onkey(u,"Up")
        turtle.onkey(l,"Left")
        turtle.onkey(r,"Right")
        turtle.onkey(d,"Down")
        turtle.listen()
        move()
        x = turtle.xcor()
        y = turtle.ycor()        
        if x > foodcoord[0]*20-5 and x < foodcoord[0]*20+5 and y > foodcoord[1]*20-5 and y < foodcoord[1]*20+5:
            foodcoord[2] = 0
            tfood.clear()
            a[0] += 1
            tscore.clear()
            tscore.write("Score:" + str(a[0]), align="center",font=(10))
        
        if len(cpos) > 1:
            for i in range(1,len(cpos)):
                if x < cpos[i][0]+5 and x > cpos[i][0]-5 and y < cpos[i][1]+5 and y > cpos[i][1]-5:
                        tscore.clear()
                        tfood.clear()
                        gameover()
    tscore.clear()
    tfood.clear()
    gameover()


#Food
def food(tfood):
    x = random.randrange(-8,8,1)
    y = random.randrange(-8,8,1)
    foodcoord[0] = x
    foodcoord[1] = y
    tfood.hideturtle()
    tfood.pu()
    tfood.shape("square")
    tfood.color("blue")
    tfood.goto(x*20,y*20)
    tfood.stamp()

#Up   
def u():
    if head[0] == 270:
        pass
    else:
        head[0] = 90
#Down
def d():
    if head[0] == 90:
        pass
    else:
        head[0] = 270
#Left
def l():
    if head[0] == 0:
        pass
    else:
        head[0] = 180
#Right
def r():
    if head[0] == 180:
        pass
    else:
        head[0] = 0

def move():
    turtle.pensize(1)
    turtle.color("green")
    turtle.pu()
    turtle.speed(3)
    turtle.setheading(head[0])
    turtle.shape("square")
    turtle.stamp()
    turtle.fd(20)
    x = turtle.xcor()
    y = turtle.ycor()
    if b[0] > a[0]:     
        turtle.clearstamps(1)
        cpos.insert(0,[round(x),round(y)])
        cpos.pop(-1)
    else:
        cpos.insert(0,[round(x),round(y)])       
        b[0] += 1    
    
def gameover():
    turtle.onscreenclick(None)
    turtle.speed(0)
    turtle.pu()
    turtle.goto(0,150)
    turtle.color("red")
    turtle.write("Sorry, game over",align="center", font=(15))
    turtle.goto(0,50)
    turtle.write("Your Score:" + str(a[0]),align="center",font=(10))
    turtle.goto(200,-200)
    turtle.write("Click to return",align="right",font=(0.0000001))
    turtle.onscreenclick(home)
    turtle.mainloop()
    
        


if __name__ == '__main__':
    home(0,0)
