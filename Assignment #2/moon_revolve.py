GlowScript 2.7 VPython

#Create Objects
Earth=sphere(pos=vec(0,1.5e11,0),radius=6.4e9,texture=textures.earth,make_trail=True)
Earth.mass=5.97e24
Earth.v=vec(-29783,0,0)

Sun=sphere(pos=vec(0,0,0),radius=3.5e10, color=color.yellow)
Sun.mass=1.99e30
Sun.v=vec(0,0,0)

#Physical properties
G=6.67e-11

#time
t=0
dt=60*24

#Simulation loop
while t<10*365*24*60*60:
    rate(1000)
    r=Earth.pos-Sun.pos
    Earth.f=-G*Earth.mass*Sun.mass/mag(r)**2*norm(r)
    Earth.v=Earth.v+Earth.f/Earth.mass*dt
    Earth.pos=Earth.pos+Earth.v*dt
    t=t+dt
