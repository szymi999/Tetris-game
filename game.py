import pygame, sys, time
from block import Block
from next import Next


class Game():

    def __init__(self):
        # Initialization
        pygame.init()
        self.screen = pygame.display.set_mode((360, 440))
        self.highscore = self.load_highscore()
        pygame.display.set_caption('Tetris, HighScore: {}'.format(self.highscore))
        self.picture = pygame.image.load('Mapa.png')
        self.play = 1
        self.points = 0
        self.ttime = 0.0
        self.font = pygame.font.Font('freesansbold.ttf', 16)
        self.text1 = self.font.render("Score: {}".format(str(self.points)), True, (80, 80, 80))
        self.text2 = self.font.render("Next: ", True, (80, 80, 80))
        self.text3 = self.font.render("Time: {}".format(self.ttime), True, (80, 80, 80))
        self.next = Next(self)
        self.block = Block(self, self.next.nr)
        self.next = Next(self)
        self.clock = pygame.time.Clock()
        self.delta = 0.0
        self.speed = 1.0
        self.max_tps = self.speed
        self.field = []
        self.mmenu = 1

        while self.menu():
            pass

        # Handle events
        while self.play:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    while self.menu():
                        pass
                        self.delta -= self.clock.tick() / 1000
                self.block.tick(event)
            self.delta += self.clock.tick()/1000
            self.max_tps = self.speed
            while self.delta > 1/self.max_tps:
                self.delta -= 1/self.max_tps
                self.lay()
                self.block.move()
                self.ttime += 1/self.max_tps
                self.points += 1/self.max_tps

            # Drawing
            self.draw()

    def load_highscore(self):
        try:
        	f = open("highscore.txt", "r+")
        	a = int(f.read())
        except FileNotFoundError:
        	a = 0
        return a

    def save_highscore(self):
        f = open("highscore.txt", "w+")
        if self.points > self.highscore:
            f.write(str(round(self.points)))
        f.close()

    def menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if self.mmenu == 1:
                    return False
                if self.mmenu == 2:
                    sys.exit(0)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                self.mmenu += 1
                if self.mmenu == 3:
                    self.mmenu = 1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.mmenu -= 1
                if self.mmenu == 0:
                    self.mmenu = 2

        self.screen.fill((0, 0, 0))
        self.screen.blit(self.picture, (0, 0))
        self.font = pygame.font.Font('freesansbold.ttf', 16)
        self.text1 = self.font.render("Score: {}".format(round(self.points)), True, (80, 80, 80))
        self.text2 = self.font.render("Next:", True, (80, 80, 80))
        self.text3 = self.font.render("Time: {}".format(round(self.ttime)), True, (80, 80, 80))
        self.screen.blit(self.text1, (243, 133))
        self.screen.blit(self.text2, (273, 183))
        self.screen.blit(self.text3, (243, 273))
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.text4 = self.font.render("TETRIS", True, (80, 80, 80))
        self.screen.blit(self.text4, (60, 40))
        self.font = pygame.font.Font('freesansbold.ttf', 16)
        if self.mmenu == 1:
            self.text5 = self.font.render("Play", True, (0, 255, 0))
            self.text6 = self.font.render("Quit", True, (80, 80, 80))
        if self.mmenu == 2:
            self.text5 = self.font.render("Play", True, (80, 80, 80))
            self.text6 = self.font.render("Quit", True, (0, 255, 0))
        self.screen.blit(self.text5, (60, 100))
        self.screen.blit(self.text6, (60, 140))
        pygame.display.flip()
        return True

    def lay(self):
        for i in self.block.f:
            if i.y >= self.check_field_height(i) - 20:
                if i.y <=22:
                    self.game_over()
                else:
                    for j in self.block.f:
                        self.field.append(j)
                self.field_sort()
                self.add_points()
                del self.block
                self.block = Block(self, self.next.nr)
                del self.next
                self.next = Next(self)
                break

    def add_points(self):
        a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] # ile jest kwadratow w wierszu
        self.ify(a)
        b = 0
        for i in a:
            b+=i
            if i == 10:
                b-=10
                self.points+=100
                self.speed+=0.2
                self.deleting(b)
                for j in range(b):
                    self.field[j].y += 20

    def deleting(self, b):
        for i in range(b, b+10):
            self.field.pop(b)

    def ify(self, a):  # nadanie wartosci tablicy a
        for i in self.field:
            for j in range(len(a)):
                if i.y == 22 + j*20:
                    a[j]+=1

    def check_field_height(self, i):
        a = 422
        for j in self.field:
            if j.x == i.x:
                if j.y == i.y+20:
                    a = j.y
        return a

    def field_sort(self):
        for i in range(len(self.field)):
            for j in range(len(self.field)):
                if j == 0:
                    continue
                if self.field[j].y<self.field[j-1].y:
                    wieksza = self.field[j-1]
                    self.field[j-1] = self.field[j]
                    self.field[j] = wieksza

    def game_over(self):
        self.play = 0
        print("Game over, Score: {}, Time: {}".format(round(self.points), round(self.ttime)))
        self.save_highscore()
        self.font = pygame.font.Font('freesansbold.ttf', 40)
        text1 = self.font.render("Game Over", True, (255, 0, 0))
        self.font = pygame.font.Font('freesansbold.ttf', 15)
        text2 = self.font.render("Nacisnij spacje aby wyjsc", True, (255, 0, 0))
        self.screen.blit(text1, (40, 60))
        self.screen.blit(text2, (40, 140))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    sys.exit(0)
                if event.type == pygame.QUIT:
                    sys.exit(0)



    def draw(self):
        self.font = pygame.font.Font('freesansbold.ttf', 16)
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.picture, (0, 0))
        self.text1 = self.font.render("Score: {}".format(round(self.points)), True, (80, 80, 80))
        self.text2 = self.font.render("Next:", True, (80, 80, 80))
        self.text3 = self.font.render("Time: {}".format(round(self.ttime)), True, (80, 80, 80))
        self.screen.blit(self.text1, (243, 133))
        self.screen.blit(self.text2, (273, 183))
        self.screen.blit(self.text3, (243, 273))
        self.block.draw()
        for i in self.field:
            pygame.draw.rect(self.screen, (0,0,255), (i.x, i.y, 15, 15), 5)
        self.next.draw()
        pygame.display.flip()


if __name__ == '__main__':
    Game()