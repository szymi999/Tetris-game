import pygame


class Block():

    def __init__(self, game, nr):
        self.game = game
        self.nr = nr
        self.y = [pygame.math.Vector2(0, 0), pygame.math.Vector2(0, 0), pygame.math.Vector2(0, 0), pygame.math.Vector2(0, 0)]
        self.f = [pygame.math.Vector2(0, 0), pygame.math.Vector2(0, 0), pygame.math.Vector2(0, 0), pygame.math.Vector2(0, 0)]
        self.vec = [pygame.math.Vector2(102, -58)]
        self.figure()
        self.up = 0
        for i in range(4):
            self.f[i] = self.y[i] + self.vec[0]

    def move(self):
        self.vec[0].y += 20
        for i in range(4):
            self.f[i] = self.y[i] + self.vec[0]

    def height(self):
        a = self.f[0].y
        for i in self.f:
            if i.y > a:
                a = i.y
        return a

    def tick(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            self.rotate()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            self.game.speed += 4.0
        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            self.game.speed -= 4.0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if self.check_if_able_right():
                self.vec[0].x += 20
                for i in range(4):
                    self.f[i] = self.y[i] + self.vec[0]
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if self.check_if_able_left():
                self.vec[0].x -= 20
                for i in range(4):
                    self.f[i] = self.y[i] + self.vec[0]

    def check_if_able_right(self):
        for j in self.f:
            if j.x+20==222:
                return False
            for a in self.game.field:
                if j.y==a.y and j.x+20==a.x:
                    return False
        return True

    def check_if_able_left(self):
        for j in self.f:
            if j.x==22:
                return False
            for a in self.game.field:
                if j.y==a.y and j.x-20==a.x:
                    return False
        return True

    def rotate(self):
        self.y = [p.rotate(90) for p in self.y]
        for i in range(4):
            self.f[i] = self.y[i] + self.vec[0]
        if self.check_if_rotate():
            for i in range(3):
                self.y = [p.rotate(90) for p in self.y]
        for i in range(4):
            self.f[i] = self.y[i] + self.vec[0]

    def check_if_rotate(self):
        for i in self.f:
            if i.x >=222 or i.x < 22:
                return True
            for a in self.game.field:
                if i.y==a.y and i.x==a.x:
                    return True
        return False

    def draw(self):
        for i in range(4):
            self.f[i] = self.y[i] + self.vec[0]
        for i in self.f:
            if i.y < 20:
                continue
            pygame.draw.rect(self.game.screen, (0, 0, 255), pygame.Rect(i.x, i.y, 15, 15),5)

    def figure(self):
        if self.nr == 1:
            self.y = [pygame.math.Vector2(-20, 20), pygame.math.Vector2(0, 20), pygame.math.Vector2(0, 0), pygame.math.Vector2(-20, 0)]
        if self.nr == 2:
            self.y = [pygame.math.Vector2(-20, 0), pygame.math.Vector2(0, 0), pygame.math.Vector2(20, 0), pygame.math.Vector2(0, -20)]
        if self.nr == 3:
            self.y = [pygame.math.Vector2(-20, 0), pygame.math.Vector2(0, 0), pygame.math.Vector2(20, 0), pygame.math.Vector2(40, 0)]
        if self.nr == 4:
            self.y = [pygame.math.Vector2(-20, 20), pygame.math.Vector2(-20, 0), pygame.math.Vector2(0, 0), pygame.math.Vector2(0, -20)]
        if self.nr == 5:
            self.y = [pygame.math.Vector2(-20, -20), pygame.math.Vector2(-20, 0), pygame.math.Vector2(0, 0), pygame.math.Vector2(0, 20)]
        if self.nr == 6:
            self.y = [pygame.math.Vector2(-20, 0), pygame.math.Vector2(0, 0), pygame.math.Vector2(20, 0), pygame.math.Vector2(20, -20)]
        if self.nr == 7:
            self.y = [pygame.math.Vector2(-20, -20), pygame.math.Vector2(-20, 0), pygame.math.Vector2(0, 0), pygame.math.Vector2(20, 0)]
        for i in range(4):
            self.f[i] = self.y[i] + self.vec[0]
