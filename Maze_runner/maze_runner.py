import turtle as tu
def make_grid():
	t.pu()
	t.seth(90)
	for i in range(Dimensions+1):
		t.setpos(i*scale+Correct,0+Correct)
		t.pd()
		t.fd(Dimensions*scale)
		t.pu()
	t.seth(0)
	for i in range(Dimensions+1):
		t.setpos(0+Correct,i*scale+Correct)
		t.pd()
		t.fd(Dimensions*scale)
		t.pu()
	t.setpos(int(Dimensions/2)*scale+Correct,int(Dimensions/2)*scale+Correct)
	t.pd()
	t.color("gold")
	for i in range(4):
		t.pensize(3)
		t.fd(scale*2)
		t.left(90)
	t.pensize(1.5)
	t.color("cyan")
	t.pu()
	t.setpos(300,-40)
	t.pd()
	t.circle(20)
def check_consecutive(a,b):
	if None in a+b:
		return False
	if a[0]==b[0]:
		if b[1]-a[1] in[0,1,-1]:
			return True
	if a[1]==b[1]:
		if a[0]-b[0] in [1,-1]:
			return True
	return False
def open_box(b1,b2,l):
	if -1 not in b1+b2 and None not in b1+b2:
		b1_index=b1[0]+Dimensions*b1[1]
		b2_index=b2[0]+Dimensions*b2[1]
		if b1[0]==b2[0]:
			if b2[1]>b1[1]:
				l[b1_index][0],l[b2_index][2]=1,1
			else:
				l[b2_index][0],l[b1_index][2]=1,1
		if b1[1]==b2[1]:
			if b2[0]>b1[0]:
				l[b1_index][1],l[b2_index][3]=1,1
			else:
				l[b2_index][1],l[b1_index][3]=1,1
			if b1[0]==b2[0]:
				l[b2_index]=[1,1,1,1]
def update_grid(l):
	for i in range(len(l)):
		for j in range(4):
			if l[i][j]:
				x=i%Dimensions
				y=i//Dimensions
				t.pu()
				if j==0:
					t.setpos(x*scale+Correct,(y+1)*scale+Correct)
					t.seth(0)
					t.pd()
					t.fd(scale)
					t.pu()
				elif j==1:
					t.setpos((x+1)*scale+Correct,(y+1)*scale+Correct)
					t.seth(-90)
					t.pd()
					t.fd(scale)
					t.pu()
				elif j==2:
					t.setpos((x)*scale+Correct,(y)*scale+Correct)
					t.seth(0)
					t.pd()
					t.fd(scale)
					t.pu()
				elif j==3:
					t.setpos((x)*scale+Correct,(y)*scale+Correct)
					t.seth(90)
					t.pd()
					t.fd(scale)
					t.pu()
def main(x,y):
	if (x-300)**2+(y+20)**2 <=400:
		find_paths(gameboard)
	global box1,box2
	x1=x2=y1=y2=None
	# for getting x cor of the box
	for i in range(0,Dimensions):
		if i*scale +scale/4 <=x-Correct<=(i+1)*scale-scale/4:
			x1=x2=i
		if i*scale +scale/4 <=y-Correct<=(i+1)*scale-scale/4:
			y1=y2=i
		if i*scale-scale*5/20<=x-Correct<=i*scale+scale*5/20 and not(i*scale-scale*5/20<=y-Correct<=i*scale+scale*5/20):
			x1=i-1
			x2=i
		if i*scale+scale*5/20<=y-Correct <=(i+1)*scale-scale*5/20:
			y1=i
			y2=i
	if None in [x1,x2,y1,y2]:
		for i in range(0,Dimensions):
			if not(i*scale-scale*5/20<=x -Correct<=i*scale+scale*5/20) and (i*scale-scale*5/20<=y-Correct <=i*scale+scale*5/20):
				y1=i-1
				y2=i
			if i*scale+scale*5/20<=x-Correct <=(i+1)*scale+scale*5/20:
				x1=i
				x2=i
	box1=(x1,y1)
	box2=(x2,y2)
	main2()
def main2():
	if check_consecutive(box1,box2):
		open_box(box1,box2,gameboard)
		update_grid(gameboard)
def find_paths(gameboard):
	paths=[]
	paths.append([(0,0)])
	paths=add_path(paths)
	paths=conv_to_normal(paths)
	Correct_paths=find_correct_paths(paths)
	if len(Correct_paths)==0:
		return
	min_length=len(Correct_paths[0])
	min_path=Correct_paths[0]
	for i in range(len(Correct_paths)):
		if len(Correct_paths[i])<min_length:
			min_path=Correct_paths[i]
			min_length=len(Correct_paths[i])
	complete_puzzle(min_path)
def add_path(path,last_move=None):
	for i in range(len(path)):
		if (path[len(path)-1][-1][0],path[len(path)-1][-1][1]) in [(path[-1][i][0],path[-1][i][1]) for i in range(len(path[-1])-1)]+[(int(Dimensions/2),int(Dimensions/2)),(int(Dimensions/2)+1,int(Dimensions/2)),(int(Dimensions/2),int(Dimensions/2)+1),(int(Dimensions/2)+1,int(Dimensions/2)+1)]:
			break
		l=path[-1]
		index_in_board=path[-1][-1][0]+path[-1][-1][1]*Dimensions
		no_of_ways=0
		for j in range(4):
			if gameboard[index_in_board][j]:
				no_of_ways+=1
		if last_move !=None:
			no_of_ways-=1
		if no_of_ways>0:
			del path[-1]
			for j in range(4):
				if gameboard[index_in_board][j]:
					if j==0 and last_move!=2:
						path.append(add_path([l+[(l[-1][0],l[-1][1]+1)]],0))
					if j==1 and last_move!=3:
						path.append(add_path([l+[(l[-1][0]+1,l[-1][1])]],1))
					if j==2 and last_move!=0:
						path.append(add_path([l+[(l[-1][0],l[-1][1]-1)]],2))
					if j==3 and last_move!=1:
						path.append(add_path([l+[(l[-1][0]-1,l[-1][1])]],3))
	return path
def conv_to_normal(lis):
	st=str(lis)
	li=[]
	l=[]
	for i in range(len(st)):
		if st[i]=="(":
			l.append((int(st[i+1]),int(st[i+4])))
		if st[i]=="]" and l!=[]:
			li.append(l)
			l=[]
	return li
def find_correct_paths(paths):
	Correct_paths=[]
	for i in paths:
		if i[-1] in [(int(Dimensions/2),int(Dimensions/2)),(int(Dimensions/2)+1,int(Dimensions/2)),(int(Dimensions/2),int(Dimensions/2)+1),(int(Dimensions/2)+1,int(Dimensions/2)+1)]:
			Correct_paths.append(i)
	return Correct_paths			
def complete_puzzle(path):
	t.pu()
	t.setpos(0*scale+Correct+scale/2,0*scale+Correct+scale/2)
	t.shape('turtle')
	t.speed(3)
	t.color("lime")
	tu.tracer(1)
	for i in range(len(path)-1):
		set_heading(i,path)
		t.fd(scale)
	t.left(360*2)
	t.color("black")
	t.shape("blank")
	t.speed(0)
	tu.tracer(20)
def set_heading(index,path):
	if path[index][0]==path[index+1][0]+1:
		t.seth(180)
	elif path[index][0]==path[index+1][0]-1:
		t.seth(0)
	elif path[index][1]==path[index+1][1]+1:
		t.seth(-90)
	elif path[index][1]==path[index+1][1]-1:
		t.seth(90)
screen=tu.Screen()
t=tu.Turtle()
screen.bgcolor("black")
t.shape("blank")
t.color("cyan")
t.speed(0)
tu.tracer(25)
Dimensions=8
scale=400/Dimensions
Correct=-Dimensions*scale/2
gameboard=[[0,0,0,0] for i in range(Dimensions**2)]
make_grid()
t.color("black")
box1=box2=None
while True:
	screen.onclick(main)
	tu.mainloop()
