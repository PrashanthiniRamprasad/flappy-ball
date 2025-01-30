import pgzrun
import random

WIDTH = 500
HEIGHT = 600
GRAVITY = 1000

class Beyonce:
  def __init__(self,x,y,radius,color):
    self.x = x
    self.y = y
    self.radius = radius
    self.color = color
    self.vx = 200
    self.vy = 0
  
  def draw(self):
    pos = self.x,self.y
    screen.draw.filled_circle(pos,self.radius,self.color)

ball = Beyonce(50,60,30,"blue")
ball2 = Beyonce(80,40,25,"red")

def draw():
  screen.clear()
  ball.draw()
  ball2.draw()

# def update(dt):
#   uy = ball.vy
#   ball.vy = GRAVITY*dt
#   ball.y += (uy + ball.vy)*0.5*dt

#   if ball.y > HEIGHT-ball.radius:
#     ball.y = HEIGHT-ball.radius
#     ball.vy = -ball.vy*0.7

#   ball.x += ball.vx*dt  
#   if ball.x > WIDTH-ball.radius or ball.x < ball.radius:
#     ball.vx = -ball.vx



# def on_key_down(key):
#   if key == keys.SPACE:
#     ball.vy = -400
 
def update(dt): # delta time- very small time duration
        
    # Apply constant acceleration formulae    
    uy = ball.vy # uy = current vertical velocity of ball
    ball.vy += GRAVITY * dt #(v=u+at) ball's vertical velocity increases due to the acc. of gravity 
    ball.y += (uy + ball.vy) * 0.5 * dt #(s = ut + 1/2 at^2)  - calculate avg. velocity over the time interval dt
    # detect and handle bounce
    if ball.y > HEIGHT - ball.radius:  # we've bounced!
        ball.y = HEIGHT - ball.radius  # fix the position
        ball.vy = -ball.vy * 0.9  # inelastic collision
    # X component doesn't have acceleration
    ball.x += ball.vx * dt
    if ball.x > WIDTH - ball.radius or ball.x < ball.radius:
        ball.vx = -ball.vx

    #ball2
    uy = ball2.vy # uy = current vertical velocity of ball
    ball2.vy += GRAVITY * dt #(v=u+at) ball's vertical velocity increases due to the acc. of gravity 
    ball2.y += (uy + ball2.vy) * 0.5 * dt #(s = ut + 1/2 at^2)  - calculate avg. velocity over the time interval dt
    # detect and handle bounce
    if ball2.y > HEIGHT - ball2.radius:  # we've bounced!
        ball2.y = HEIGHT - ball2.radius  # fix the position
        ball2.vy = -ball2.vy * 0.9  # inelastic collision
    # X component doesn't have acceleration
    ball2.x += ball2.vx * dt
    if ball2.x > WIDTH - ball2.radius or ball2.x < ball2.radius:
        ball2.vx = -ball2.vx    

def on_key_down(key):
    """Pressing a key will kick the ball upwards."""
    if key == keys.SPACE:
        ball.vy = -500
        ball2.vy = -500
pgzrun.go()  