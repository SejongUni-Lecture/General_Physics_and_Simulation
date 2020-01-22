GlowScript 2.7 VPython

obj=box(size=vec(0.5,0.25,0.25), color=color.yellow)
obj.pos=vec(-5,0,0)
obj.v=vec(0,0,0)
obj.a=vec(1,0,0)

t=0
dt=0.01

attach_trail(obj,type="points",pps=5,color=color.yellow)

while t<5:
    rate(1/dt)
    obj.v=obj.v+obj.a*dt
    obj.pos=obj.pos+obj.v*dt
    t=t+dt
