import pygame as p

# minebloc 0.0.1
screen = p.display.set_mode((350, 300))

class cursor:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __create__(self):
        p.draw.rect(screen,"white",p.Rect(self.x,self.y,50,50))

Csr=cursor(x=100,y=100)

class player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __create__(self):
        p.draw.rect(screen, "black", p.Rect(self.x, self.y, 50, 100))

pl1 = player(x=100, y=150)

class block:
    def __init__(self, x, y, color="green"):
        self.x = x
        self.y = y
        self.color = color

    def __create__(self):
        p.draw.rect(screen, self.color, p.Rect(self.x, self.y, 50, 50))



bl1 = block(0, 250)
bl2 = block(50, 250)
bl3 = block(100, 250)
bl4 = block(150, 250)
bl5 = block(200, 250)
bl6 = block(250, 250)
bl7 = block(300, 250)
bl8 = block(350, 250)
bl9 = block(400, 250)

# pygame setup
p.init()

clock = p.time.Clock()
running = True


class main:
    while running:
        p.display.set_caption('minebloc')
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
            if event.type==p.KEYDOWN:
                if event.key == p.K_RIGHT: pl1.x += 25
                if event.key == p.K_LEFT: pl1.x -= 25
                if event.key == p.K_d:Csr.x+=50
                if event.key == p.K_q:Csr.x-=50
                if event.key == p.K_z:Csr.y-=50
                if event.key == p.K_s:Csr.y+=50
                if Csr.x==bl1.x and Csr.y==bl1.y and event.key==p.K_r:bl1.x=1000;screen.fill("blue")
                if Csr.x==bl2.x and Csr.y==bl2.y and event.key==p.K_r:bl2.x=1000;screen.fill("blue")
                if Csr.x==bl3.x and Csr.y==bl3.y and event.key==p.K_r:bl3.x=1000;screen.fill("blue")
                if Csr.x==bl4.x and Csr.y==bl4.y and event.key==p.K_r:bl4.x=1000;screen.fill("blue")
                if Csr.x==bl5.x and Csr.y==bl5.y and event.key==p.K_r:bl5.x=1000;screen.fill("blue")
                if Csr.x==bl6.x and Csr.y==bl6.y and event.key==p.K_r:bl6.x=1000;screen.fill("blue")
                if Csr.x==bl7.x and Csr.y==bl7.y and event.key==p.K_r:bl7.x=1000;screen.fill("blue")
                if Csr.x==bl8.x and Csr.y==bl8.y and event.key==p.K_r:bl8.x=1000;screen.fill("blue")
                if Csr.x==bl9.x and Csr.y==bl9.y and event.key==p.K_r:bl9.x=1000;screen.fill("blue")

        
        screen.fill("blue")

        
        bl1.__create__()
        bl2.__create__()
        bl3.__create__()
        bl4.__create__()
        bl5.__create__()
        bl6.__create__()
        bl7.__create__()
        bl8.__create__()
        pl1.__create__()
        Csr.__create__()

        
        p.display.flip()

        clock.tick(60)  


p.quit()
