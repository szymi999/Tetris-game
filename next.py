import random, pygame


class Next():

    def __init__(self, game):
        self.game = game
        self.nr = random.randint(1, 7)
        self.f = [pygame.math.Vector2(283, 205), pygame.math.Vector2(0, 0), pygame.math.Vector2(0, 0),pygame.math.Vector2(0, 0)]
        self.figure()

    def draw(self):
        for i in self.f:
            pygame.draw.rect(self.game.screen, (0,200,200), pygame.Rect(i.x, i.y, 10, 10), 1)

    def figure(self):
        if self.nr == 1:
            self.f[1] = pygame.math.Vector2(self.f[0].x+10, self.f[0].y)
            self.f[2] = pygame.math.Vector2(self.f[0].x, self.f[0].y+10)
            self.f[3] = pygame.math.Vector2(self.f[0].x+10, self.f[0].y+10)
        if self.nr == 2:
            self.f[1] = pygame.math.Vector2(self.f[0].x - 10, self.f[0].y+10)
            self.f[2] = pygame.math.Vector2(self.f[0].x, self.f[0].y+10)
            self.f[3] = pygame.math.Vector2(self.f[0].x + 10, self.f[0].y + 10)
        if self.nr == 3:
            self.f[1] = pygame.math.Vector2(self.f[0].x+10, self.f[0].y)
            self.f[2] = pygame.math.Vector2(self.f[0].x+20, self.f[0].y)
            self.f[3] = pygame.math.Vector2(self.f[0].x-10, self.f[0].y)
        if self.nr == 4:
            self.f[1] = pygame.math.Vector2(self.f[0].x, self.f[0].y + 10)
            self.f[2] = pygame.math.Vector2(self.f[0].x - 10, self.f[0].y + 10)
            self.f[3] = pygame.math.Vector2(self.f[0].x - 10, self.f[0].y + 20)
        if self.nr == 5:
            self.f[1] = pygame.math.Vector2(self.f[0].x, self.f[0].y + 10)
            self.f[2] = pygame.math.Vector2(self.f[0].x + 10, self.f[0].y + 10)
            self.f[3] = pygame.math.Vector2(self.f[0].x + 10, self.f[0].y + 20)
        if self.nr == 6:
            self.f[0].y += 10
            self.f[1] = pygame.math.Vector2(self.f[0].x-10, self.f[0].y)
            self.f[2] = pygame.math.Vector2(self.f[0].x+10, self.f[0].y)
            self.f[3] = pygame.math.Vector2(self.f[0].x+10, self.f[0].y-10)
        if self.nr == 7:
            self.f[1] = pygame.math.Vector2(self.f[0].x, self.f[0].y+10)
            self.f[2] = pygame.math.Vector2(self.f[0].x+10, self.f[0].y+10)
            self.f[3] = pygame.math.Vector2(self.f[0].x+20, self.f[0].y+10)