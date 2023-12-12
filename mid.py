

from tkinter import *
import threading , random
import time


def drawclosebar(w):

    if lor == 0 :
        w.delete('block_r')
        x=450; y=300; w1=35; w2=20;
        w.create_rectangle(325-139,210,325+139,300+90,fill="green",width=0 ,tags='block_r')
        w.create_rectangle(x-w1+100,y-w2-20,x+w1+100,y+w2-20,fill="DarkViolet",width=3,outline="black",tags='block_r')
        w.create_rectangle(x-w1+100,y-w2+20,x+w1+100,y+w2+20,fill="SkyBlue",width=3,outline="black",tags='block_r')
        y=0; w1=25; w2=240;
        w.create_rectangle(x-w1+100,y-w2+20,x+w1+100,y+w2+20,fill="white",width=3,outline="black",tags='block_r')
        y=440; w2=120;
        w.create_rectangle(x-w1+100,y-w2+20,x+w1+100,y+w2+40,fill="white",width=3,outline="black",tags='block_r')
        w.delete('block_r')
    else:
        w.delete('block_l')
        x=20; y=300; w1=35; w2=20;
        w.create_rectangle(x-w1+100,y-w2+20,x+w1+100,y+w2+20,fill="SkyBlue",width=3,outline="black",tags='block_l')
        w.create_rectangle(x-w1+100,y-w2-20,x+w1+100,y+w2-20,fill="DarkViolet",width=3,outline="black",tags='block_l')
        y=0; w1=25; w2=240;
        w.create_rectangle(x-w1+100,y-w2+20,x+w1+100,y+w2+40,fill="white",width=3,outline="black",tags='block_l')
        y=480; w1=25; w2=120;
        w.create_rectangle(x-w1+100,y-w2+20,x+w1+100,y+w2+100,fill="white",width=3,outline="black",tags='block_l')
        w.create_rectangle(0,290,205,300,fill="green",width=0,tags='block_l')
        w.delete('block_l')

def drawopenber(w):
    #right
    x=450; y=260; w1=35; w2=20;
    w.create_rectangle(x-w1+100,y-w2-20,x+w1+100,y+w2-20,fill="DarkViolet",width=3,outline="black",tags='block_r')
    w.create_rectangle(x-w1+100,y-w2+20+80,x+w1+100,y+w2+20+80,fill="SkyBlue",width=3,outline="black",tags='block_r')
    y=0; w1=25; w2=600/2-120;
    w.create_rectangle(x-w1+100,y-w2+20,x+w1+100,y+w2+40,fill="white",width=3,outline="black",tags='block_r')
    y=480; w1=25; w2=120;
    w.create_rectangle(x-w1+100,y-w2+20,x+w1+100,y+w2+100,fill="white",width=3,outline="black",tags='block_r')
    w.create_rectangle(325-139,300-39,325+139,300+39,fill="green",width=0,tags='block_r')
    #left
    x=20; y=260; w1=35; w2=20;
    w.create_rectangle(x-w1+100,y-w2-20,x+w1+100,y+w2-20,fill="DarkViolet",width=3,outline="black",tags='block_l')
    w.create_rectangle(x-w1+100,y-w2+20+80,x+w1+100,y+w2+20+80,fill="SkyBlue",width=3,outline="black",tags='block_l')
    y=0; w1=25; w2=600/2-120;
    w.create_rectangle(x-w1+100,y-w2+20,x+w1+100,y+w2+40,fill="white",width=3,outline="black",tags='block_l')
    y=480; w1=25; w2=120;
    w.create_rectangle(x-w1+100,y-w2+20,x+w1+100,y+w2+100,fill="white",width=3,outline="black",tags='block_l')
    w.create_rectangle(0,290,205,300,fill="green",width=0,tags='block_l')
 
def rightClick(event):
    global flag
    flag=~flag
    print(flag)
    
def switch(event):
    global lor 
    lor =~ lor
    print(lor)

def drawfrog(w,x1,y1,ox,oy):
    global sw; global img; global img1;

    w.create_rectangle(ox,oy,ox+82,oy+60,fill="green",width=0)
    if sw==0:
        w.create_image(x1,y1,anchor=NW,image=img1)
    else:
        w.create_image(x1,y1,anchor=NW,image=img2)
    sw=~sw
    
def draw(w):
    global flag , sw , score , life , attack ,ran, gametimes,ti

    tmp_life = "life : %s" % (life)
    w.create_text(10,0,text=tmp_life, anchor='nw',font=('Arial',14) , tags = 're')
    tmp_score = "score : %s" % (score)
    w.create_text(300,0,text=tmp_score , anchor='nw',font=('Arial',14),tags = 're')
    w.create_text(300,300,text=ti, anchor='nw',font=('Arial',30) , tags = 'time')

    drawopenber(w)
    x=325; y=100; ox=x; oy=y;
    while True:
        if flag!=0:
            drawfrog(w, x, y, ox, oy)
            drawclosebar(w);
            if (x>450 and x<600 and lor == 0) or (x>0 and x<200 and lor == -1):
                w.delete('re')
                life -= attack
                tmp_life = "life : %s" % (life)
                w.create_text(10,0,text=tmp_life, anchor='nw',font=('Arial',14) , tags = 're')
                score += 10
                tmp_score = "score : %s" % (score)
                w.create_text(300,0,text=tmp_score , anchor='nw',font=('Arial',14),tags = 're')
                w.create_image(x,y,anchor=NW,image=img3)
            else:
                w.delete('re')
                life+=100
                tmp_life = "life : %s" % (life)
                score-=10
                tmp_score = "score : %s" % (score)
                w.create_text(300,0,text=tmp_score , anchor='nw',font=('Arial',14),tags = 're')
                w.create_text(10,0,text=tmp_life, anchor='nw',font=('Arial',14) , tags = 're')
                
            flag=~flag;
            time.sleep(0.01)

        drawopenber(w)
        drawfrog(w, x, y, ox, oy)

        ox=x; oy=y;
        if ran == 0 :
            x+=5;y=y+7;
        else:
            x-=6;y=y+7;

        if x>450:
            y=280;
        elif x < 190:
            y=280;

        if x>600 or x < 10:
            ran = random.randint(0,1)
            x=325; y=100;
        if life == 0 :
            if gametimes == 5 :
                ti = 0
                w.create_text(180,250,text='YOU WIN', anchor='nw',font=('Arial',50));time.sleep(1)
                w.delete('all')
                w.create_text(180,250,text='VICTORY', anchor='nw',font=('Arial',50))
                w.create_text(180,350,text='Score:%s'%(score), anchor='nw',font=('Arial',30))
                time.sleep(1)
                root.destroy()
                break
            life = 500
            gametimes += 1
            w.delete('block_r') ; w.delete('block_l')
        if ti == 0 and gametimes != 5 :
                w.create_text(180,250,text='YOU LOSE', anchor='nw',font=('Arial',50));time.sleep(1)
                w.delete('all')
                w.create_text(180,250,text='DEFEAT', anchor='nw',font=('Arial',50))
                time.sleep(1)
                root.destroy()
                break

def timechge():
    global ti
    while True:
        w.create_text(300,300,text=ti, anchor='nw',font=('Arial',30) , tags = 'time')
        ti -= 1 
        time.sleep(1)
        w.delete('time')
        print(ti)
        if ti == 0 :
            break
        

            
sw=0
flag=0
ti=20 
score = 0 #分數
gametimes = 0
ran = 0
life = 500
attack = 100
lor = 0 #判斷左右管子
root = Tk()
w = Canvas(root,width=650,height=600,bg="green")
w.pack()

w.bind("<Button-1>",rightClick)
w.bind('<Button-3>' , switch)
img1 = PhotoImage(file="f1.png")
img2 = PhotoImage(file="f2.png")
img3 = PhotoImage(file="f3.png")

drawopenber(w)

t = threading.Thread(target = draw,args=(w,))
tt = threading.Thread(target=timechge)
t.start() ; tt.start() 

root.mainloop()
    