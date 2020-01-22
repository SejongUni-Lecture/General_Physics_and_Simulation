GlowScript 2.7 VPython

#ground
ground =box(pos=vec(0,0,0), size=vec(100,0.10,70), color=color.green)
#init position
init_pos=vec(-30,0.11,0)
ball=sphere(pos=init_pos,radius=0.11,color=color.orange, make_trail=False)
ball.m=0.45
ball.speed=25
ball.angle=radians(35)
ball.v=ball.speed*vec(cos(ball.angle), sin(ball.angle),0)
#attach_trail(ball)
attach_arrow(ball,"v",shaftwidth=0.1, scale=0.3, color=color.yellow)

scene.range=30

#goal
goal = box(pos=vec(15,1.5,0), size=vec(0.5,3,8), color=color.white)

#const
g=-9.8 #m/s**2
rho=1.204 #kg/m**3
Cd=0.3
Cm=1
w=10*2*pi #10 rev. per sec

##UI
scene.append_to_caption('\nInitial Values\n\n')
#slider
velocitySlider =slider(min=0,max=45,value=25, bind=setVelocity)
scene.append_to_caption('\nVelocity: ',velocitySlider.min, 'to', velocitySlider.max,'\n\n')

def setVelocity():
    global ball
    ball.speed=velocitySlider.value
    ball.v=ball.speed*vec(cos(ball.angle), sin(ball.angle) ,0)
    
    
angleSlider = slider(min= 0, max = 90, value = 35, bind =setAngle)

scene.append_to_caption('\nAngle: ', angleSlider.min, 'to' ,angleSlider.max, '\n\n')

def setAngle():
    global ball
    ball.angle=radians(angleSlider.value)
    ball.v=ball.speed*vec(cos(ball.angle), sin(ball.angle), 0)
    
angularSlider = slider(min=-10,max=10, value=0,bind=setAngular)

scene.append_to_caption('\nAngluar velocity:', angularSlider.min, 'to', angularSlider.max,'\n\n')

def setAngular():
    global w
    w=angularSlider.value*2*pi
    
#Buttom
btnStart = button(text = 'Shoot',bind = startbtn)

def startbtn(b):
    b.disabled = True
    return b.disabled
  
#time setting
t=0
dt=0.01

while 1:
    rate(1/dt)
    
    if btnStart.disabled == True:
        ball.make_trail = True
        #Gravity Force
        grav=ball.m*vec(0,g,0)
        
        drag = -0.5*rho*Cd*(pi*ball.radius**2)*mag(ball.v)**2*norm(ball.v)
        #Magnus Force
        magnus = 0.5*rho*Cm*(pi*ball.radius**2)*ball.radius*w*mag(ball.v)*cross(vec(0,1,0),norm(ball.v))
        #print("gravity: ", mag(grav), 'drag force: ', mag(drag), 'magnus force: ',mag(magnus))

        #Sum of forces
        ball.f=grav+drag
        
        #Time stepping
        ball.v =ball.v+ball.f/ball.m*dt
        ball.pos=ball.pos+ball.v*dt
        
        #collision
        if ball.pos.y-ball.radius<0:
            #print("distance: ", ball.pos.x-init_pos.x, "Angle: ", ball.angle*180/pi)
            #scene.waitfor('click')
            ##reset
            btnStart.disabled=False
            ball.pos=init_pos
            ball.v=ball.speed*vec(cos(ball.angle), sin(ball.angle),0)
            ball.make_trail=False
            t=0
        if 0 <= ball.pos.y <= goal.pos.y and goal.pos.x - 0.25 <=ball.pos.x<=goal.pos.x + 0.25:
            print("Goal in\n")
            break
        t=t+dt
    
 
 
    

