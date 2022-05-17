import turtle
print("the equation is in form ax^2+by^2+2hxy+2gx+2fy+c=0")
a=float(input("enter the value of a"))
b=float(input("enter the value of b"))
h=float(input("enter the value of h"))
g=float(input("enter the value of g"))
f=float(input("enter the value of f"))
c=float(input("enter the value of c"))
s=turtle.Screen()
t=turtle.Turtle()
s.bgcolor("black")
t.color("lime")
t.shape("blank")
t.speed(0)
t.fd(-1000)
t.fd(2000)
t.home()
t.left(90)
t.fd(-1000)
t.fd(2000)
t.pu()
t.color("cyan")
d=a*b*c+2*f*g*h-a*f*f-g*g*b-c*h*h
if d==0:
	print("pair of lines")
else:
	if round(h*h-a*b,3)>0:
		print("hyperbola")
	elif round(h*h-a*b,3)<0:
		if a!=b:
			print("ellipse")
		else:
			print("circle")
	else:
		print("parabola")
turtle.tracer(1000,0)
i=0
while i<=1001:			#PLOTTING WRT X-AXIS
	x=round(i-500,1)
	p=b
	q=2*f+2*h*x
	r=a*x*x+2*g*x+c
	if p!=0:
		y1=(-q-(q*q-4*p*r)**0.5)/(2*p)
		y2=(-q+(q*q-4*p*r)**0.5)/(2*p)
		if y1.imag==0:
			t.setpos(x*10,y1*10)
			t.pd()
			t.dot(size=2)
			t.pu()
			if y1==0:
				print(x)
		if y2.imag==0:
			t.setpos(x*10,y2*10)
			t.pd()
			t.dot(size=2)
			t.pu()
			if y2==0:
				print(x)
	else:
		if q!=0:
			y1=-(r/q)
			if y1.imag==0:
				t.setpos(x*10,y1*10)
				t.pd()
				t.dot(size=2)
				t.pu()
				if y1==0:
					print(x)
	i+=0.1
i=0
while i<=1001: 		#plotting wrt y-axis
	y=round(i-500,1)
	p=a
	q=2*g+2*h*y
	r=b*y*y+2*f*y+c
	if p!=0:
		x1=(-q-(q*q-4*p*r)**0.5)/(2*p)
		x2=(-q+(q*q-4*p*r)**0.5)/(2*p)
		if x1.imag==0:
			t.setpos(x1*10,y*10)
			t.pd()
			t.dot(size=2)
			t.pu()
		if x2.imag==0:
			t.setpos(x2*10,y*10)
			t.pd()
			t.dot(size=2)
			t.pu()
	else:
		if q!=0:
			x1=-(r/q)
			if x1.imag==0:
				t.setpos(x1*10,y*10)
				t.pd()
				t.dot(size=2)
				t.pu()
	i+=0.1
turtle.done()