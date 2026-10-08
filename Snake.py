import pygame
import random
pygame.init()

class Game:

    def __init__(self):
        self.grid_size = 20
        self.cell_size = 30
        self.running = True
        self.width = self.grid_size * self.cell_size
        self.height = self.grid_size * self.cell_size
        self.clock = pygame.time.Clock()
        self.speed = 10
        self.snake = Snake(10,10,"RIGHT",self.cell_size)
        self.screen = pygame.display.set_mode((self.width ,self.height))
        self.fruit = Fruit(self.grid_size,self.cell_size)
        pygame.display.set_caption("Snake")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    if self.snake.direction != "DOWN":
                        self.snake.direction = "UP"
                if event.key == pygame.K_a:
                    if self.snake.direction != "RIGHT":
                        self.snake.direction = "LEFT"
                if event.key == pygame.K_s:
                    if self.snake.direction != "UP":
                        self.snake.direction = "DOWN"
                if event.key == pygame.K_d:
                    if self.snake.direction != "LEFT":
                        self.snake.direction = "RIGHT"

    def update(self):
        self.snake.move()
        self.check_boundary_collision()
        self.check_fruit_collision()
        self.check_snake_collisison()
        pygame.display.update()

    def check_boundary_collision(self):
        head_x, head_y = self.snake.head

        if head_x >= self.grid_size :
            self.running = False

        if head_x < 0:
            self.running =  False

        if head_y >= self.grid_size :
            self.running = False

        if head_y < 0:
            self.running =  False

    def check_fruit_collision(self):
        head_x, head_y = self.snake.head

        if (head_x == self.fruit.x) & (head_y == self.fruit.y):
            self.snake.grow()
            self.fruit.generate(self.snake.body)

    def check_snake_collisison(self):
        for i in range(1,len(self.snake.body)):
            if self.snake.body[i] == self.snake.head:
                self.running = False



    def draw(self):
        #Draw Background
        self.screen.fill([30,30,30])

        #Draw Grid
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                rectangle = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, (60,60,60), rectangle, 1)

        self.snake.draw(self.screen)
        self.fruit.draw(self.screen)

    def run(self):
        while self.running :
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.speed)

        pygame.quit()


class Snake:
    def __init__(self, head_x, head_y, direction,cell_size):
        self.direction = direction
        self.cell_size = cell_size
        self.body = [(head_x, head_y)]
        self.extendBody = False

    @property
    def head(self):
        return self.body[0]

    def draw(self, screen):
        head_x, head_y = self.head
        snake_rect = pygame.Rect(head_x * self.cell_size, head_y * self.cell_size, self.cell_size, self.cell_size)
        pygame.draw.rect(screen, (0,200,0), snake_rect)
        for x,y in self.body:
            print((x,y))
            body_rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
            pygame.draw.rect(screen, (0,200,0), body_rect)

    def move(self):
        head_x, head_y = self.head
        #Adding current head position to body
        if self.extendBody:
            self.body.append((head_x,head_y))
            print("Body has been extended")
        self.extendBody = False

        if self.direction == "RIGHT":
            head_x += 1
        if self.direction == "LEFT":
            head_x += -1
        if self.direction == "UP":
            head_y += -1
        if self.direction == "DOWN":
            head_y += 1

        #Inserting new head
        self.body.insert(0,(head_x,head_y))

        #Deleting last tuple in body
        self.body.pop()

        #print("Head:(" + str(head_x) + "," + str(head_y) + ")")
        #print("Body:" + str(self.body))

    def grow(self):
        self.extendBody = True

class Fruit:
    def __init__(self,grid_size,cell_size):
        self.grid_size = grid_size
        self.cell_size = cell_size
        self.x = None
        self.y = None
        self.generate()

    def generate(self, snake_body=[]):
        while True:
            self.x = random.randrange(0, self.grid_size)
            self.y = random.randrange(0, self.grid_size)
            if (self.x, self.y) not in snake_body:
                break




    def draw(self,screen):
        fruit_rect = pygame.Rect(self.x * self.cell_size, self.y * self.cell_size, self.cell_size, self.cell_size)
        pygame.draw.rect(screen, (200,0,0), fruit_rect)



game = Game()
game.run()
