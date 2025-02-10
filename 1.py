import pygame
import time
pygame.init()

back=(200,255,255)

mw=pygame.display.set_mode((500,500))
mw.fill(back)
clock=pygame.time.Clock()

racket_x=200
racket_y=330

game_over=False

class Area():
 def __init__(self, x=0, y=0, width =10, height =10, color=None):
     self.rect = pygame.Rect(x, y, width, height)
     self.fill_color = back
     if color:
         self.fill_color = color


 def color(self, new_color):
     self.fill_color = new_color


 def fill(self):
    pygame.draw.rect(mw,self.fill_color,self.rect)


 def collidepoint(self, x, y):
     return self.rect.collidepoint(x, y)


 def colliderect(self, rect):
     return self.rect.colliderect(rect)

class Picture(Area):
    def __init__(self,filename,x=0,y=0,width=10,height=10):
        Area.__init__(self,x=x,y=y,width=width,height=height,color=None)
        self.image=pygame.transform.scale(pygame.image.load(filename), (self.rect.width, self.rect.height))
        self.health=2

    def draw(self):
        mw.blit(self.image, (self.rect.x,self.rect.y))

class Label(Area):
    def set_text(self, text,fsize=12, text_color=(0,0,0)):
        self.image = pygame.font.SysFont('verdana',fsize).render(text,True,text_color)
    def draw(self):
        self.fill()
        mw.blit(self.image, (self.rect.x,self.rect.y))
fon = Picture('macdon.png',0,0,500,500)
def restart():
    
    global ball,health,platform,start_x,start_y,count,monsters,dx,dy,move_right,move_left
    ball = Picture('rotik.png',160,200,25,25)
    platform = Picture('krutichuvak.png', racket_x, racket_y,110,70)



    start_x =5 
    start_y =5
    health = [2,2,2,2,2,2,2,2,2]
    count =9
    monsters = []
    for j in range(3):#цикл по стовпцях
        y = start_y + (55* j)#координата монстра у кожному слід. стовпці буде зміщена на 55 пікселів по y
        x = start_x + (27.5* j)#і 27.5 по x
        for i in range(count):#цикл по рядах(рядків) створює в рядку кількість монстрів,що дорівнює count
            d = Picture ('burger.png', x, y,62,62)#створюємо монстра
            monsters.append(d)#додаємо до списку
            x = x +55 #збільшуємо координату наступного монстра
        count = count -1 #для наступного ряду зменшуємо кількість монстрів

    dx=3
    dy=3

    move_right= False
    move_left= False
restart()
while not game_over:
    fon.draw()
    ball.fill()
    platform.fill()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over =True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                move_left=True
            if event.key == pygame.K_d:
                move_right=True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                move_left=False
            if event.key == pygame.K_d:
                move_right=False
    if move_left and platform.rect.x > 0:
        platform.rect.x -= 5
    if move_right and platform.rect.x < 400:
        platform.rect.x += 5
        
    if ball.rect.colliderect(platform.rect):
        dy *= -1.03

    if ball.rect.x < 0 or ball.rect.x >475:
        dx *= -1.03
    if ball.rect.y < 0:
        dy *= -1.03
    ball.rect.x +=dx
    ball.rect.y +=dy


    for m in monsters:
        m.draw()
        if m.rect.colliderect(ball.rect):
            monsters.remove(m)
            m.fill()
            dy *= -1.03

    if len(monsters)==0:
        time_text=Label(110,210,50,50,back)
        time_text.set_text('Алежа щасливий!',30,(0,200,0))
        time_text.draw()
        pygame.display.update()
        time.sleep(2)
        restart()
    if ball.rect.y>500:
        time_text=Label(5,210,50,50,back)
        time_text.set_text('Алежа злий! Він іде по тебе!',33,(200,0,0))
        time_text.draw()
        pygame.display.update()
        time.sleep(2)
        restart()


    platform.draw()
    ball.draw()

    pygame.display.update()


    clock.tick(40)




        