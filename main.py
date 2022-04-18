from pygame import *
from pong import *

bg = transform.scale(bg , (W, H))

mode = "start_screen"

def start():
    global mode
    mode = "game"

def setting():
    global mode
    mode = "setting"

def menu():
    global mode
    mode = "start_screen"

lightgreen = (0,255,100)

#class

class PlatForm():
    def __init__(self,x,y,width,height,speed,pic_name):
        self.pic = image.load(pic_name)
        self.pic = transform.scale(self.pic, (width,height))
        self.rect = Rect(x,y,width,height)
        self.speed = speed

    def update(self):
        if self.ymove == 'down':
            self.rect.y += self.speed
            if self.rect.y > H-100:
                self.rect.y = H-100
        else:
            self.rect.y -= self.speed
            if self.rect.y < 0:
                self.rect.y = 0

        self.reset()


    def reset(self):
        win.blit(self.pic,( self.rect.x,self.rect.y))



class Mychik():
    def __init__(self,x,y,w,h,speed,filename,vface,hface):
        self.speed = speed
        self.filename = filename
        self.rect = Rect(x,y,w,h)
        self.image = image.load(filename)
        self.image = transform.scale(self.image, (w,h))
        self.rect.x = x
        self.rect.y = y
        self.vface = vface
        self.hface = hface

    def reset(self):
        win.blit( self.image , (self.rect.x, self.rect.y) )

    def update(self):
        if self.hface == "right":
            self.rect.x += self.speed
            if self.rect.x > w:
                self.hface = "left"

        if self.hface == "left":
            self.rect.x -= self.speed
            if self.rect.x < 0:
                self.hface = "right"

        if self.vface == "up":
            self.rect.y -= self.speed
            if self.rect.y < 0:
                self.vface = "dawn"

        if self.vface == "dawn":
            self.rect.y += self.speed
            if self.rect.y > h:
                self.vface = "up"

        self.reset()


#start_screen
start_menu = Menu(W/2-250,H/2 - 100, "layer.png")
start_btn = Button(W/2-100,H/2,"        start", start)
settings_btn = Button(W/2-100,H/2 + 100 , "    settings", setting)
exit_btn = Button(W/2-100,H/2 + 300,"         exit", exit)

#setting
btn2560 = Button(W/2-100,H/2 ," 2560x1440",set_2560)
btn1920 = Button(W/2-100,H/2 + 100," 1920x1080",set_1920)
btn1366 = Button(W/2-100,H/2 + 200,"  1366x768",set_1366)
btn640 = Button(W/2-100,H/2 + 300,"   640x480", set_640)

res_list = ListButton(W/2-100,H/2 - 100,"      resize",[btn640, btn1366, btn1920, btn2560])
back_btn = Button(W/2-100,H/2 + 300,"        back", menu)

#game
platform = PlatForm(x=100,y=H/2,width=75*coficent,height=225*coficent,speed=10,pic_name="platform.png")
platform.ymove = "-"

platform1 = PlatForm(x=(W-100),y=H/2,width=75*coficent,height=225*coficent,speed=10,pic_name="platform.png")
platform1.ymove = "-"

ball = Mychik(H/2,W/2,75*coficent,75*coficent,10,'beach-ball-icon.png','up','right')

lightgreen = (0,255,100)


w = W
h = H

timer = time.Clock()
    
while True:

    
    for e in event.get():
        if (e.type == KEYDOWN and e.key == K_ESCAPE) or e.type == QUIT:
            exit()  
        if e.type == MOUSEBUTTONDOWN:
            if mode == "start_screen":
                start_btn.check_click(e.pos)
                settings_btn.check_click(e.pos)
                exit_btn.check_click(e.pos)
            elif mode == "setting":
                if res_list.visible == True:
                    res_list.check_click(e.pos)
                    btn640.check_click(e.pos)
                    btn1366.check_click(e.pos)
                    btn1920.check_click(e.pos)
                    btn2560.check_click(e.pos)
                else:
                    res_list.check_click(e.pos)
                    back_btn.check_click(e.pos)
        
        if e.type == KEYDOWN:
            if e.key == K_w:
                platform.ymove = "up"

            if e.key == K_s:
                platform.ymove = "down"

            if e.key == K_UP:
                platform1.ymove = "up"

            if e.key == K_DOWN:
                platform1.ymove = "down"

    if mode == "start_screen":
        win.blit(bg,(0,0))
        start_menu.update()
        start_btn.update()
        settings_btn.update()
        exit_btn.update()

    elif mode == "setting":
        if res_list.visible == True:
            win.blit(bg,(0,0))
            start_menu.update()
            res_list.update()
            btn640.update()
            btn1366.update()
            btn1920.update()
            btn2560.update()
        else:
            win.blit(bg,(0,0))
            start_menu.update()
            res_list.update()
            btn640.update()
            btn1366.update()
            btn1920.update()
            btn2560.update()
            back_btn.update()
    
    elif mode == "game":
      win.blit(bg,(0,0))
      ball.update()
      platform.update()
      platform1.update()

    timer.tick(60)
    display.update()

