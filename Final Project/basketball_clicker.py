GlowScript 2.4 VPython

count=0

#const.
g = -9.8 #m/s**2
InitPos = vec(0,17.75,40)

#ground and background
ground=box(pos=vec(0,0,0),length=60,height=1,width=85,texture=textures.wood)

scene.background=color.black
scene.camera.pos=vec(0,16,0)

#objects
    
pole=cylinder(pos=vec(0,1,-15),axis=vec(0,20,0),radius=1,color=color.white)
pole2=cylinder(pos=vec(0,20,-15),axis=vec(0,7,10),radius=1,color=color.white)
board=box(pos=vec(0,28,-4),length=15,height=10,width=0.5,color=color.white,opacity=0.5)

inline=box(pos=vec(0,28,-4.5),length =6,height=0.5,width=0.5,color=color.white)
inline2=box(pos=vec(-2.7,26,-4.5),length =0.5,height=4,width=0.5,color=color.white)
inline3=box(pos=vec(2.7,26,-4.5),length =0.5,height=4,width=0.5,color=color.white)
inline4=box(pos=vec(0,24,-4.5),length =6,height=0.5,width=0.5,color=color.white)

outline=box(pos=vec(0,32.75,-4.5),length =15,height=0.5,width=0.5,color=color.white)
outline2=box(pos=vec(7.5,28,-4.5),length =0.5,height=10,width=0.5,color=color.white)
outline3=box(pos=vec(-7.5,28,-4.5),length =0.5,height=10,width=0.5,color=color.white)
outline4=box(pos=vec(0,23.25,-4.5),length =15,height=0.5,width=0.5,color=color.white)

goal=ring(pos=vec(0,23.75,-2),axis=vec(0,1,0),radius=2.5,thickness=0.15,color=color.red)

#ball
ball=sphere(pos=InitPos,radius=1.5,color=color.orange)
ball.m = 0.155
ball.angle=36*pi/180
ball.speed=-22
ball.v = ball.speed*vec(0,-cos(ball.angle),sin(ball.angle))

#scoreboard

mylabel = label(pos = vec(0,50,0))
mylabel.text="You scored "+count+" points!"
welcome=label(pos=vec(0,60,0))
welcome.text="Click to shoot!"

#function
t=0
dt=0.03
bounce=0

scene.waitfor('click')
while (1):
    rate(100)
    
    #Gravity Force
    grav = ball.m * vec(0,g,0) #gravity
    
    ball.f=grav
    #Euler method: time stepping
    
    ball.v = ball.v + ball.f/ball.m*dt
    ball.pos = ball.pos + ball.v*dt 
 
    #collision
    if ball.pos.y - ball.radius < 0:
        ball.v.y=-0.71*ball.v.y
        count=count+1
        ball.pos=InitPos
        bounce=0
        scene.waitfor('click')
   
    mylabel.text="You scored "+count+" points!"
    t=t+dt
 
