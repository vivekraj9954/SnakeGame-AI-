import pygame
import random
import time
import sys
import csv


class snakeBody():

    def __init__(self):
        self.position = [120, 60];
        self.body = [[120, 60, 'RIGHT'], [80, 60, 'RIGHT'], [60, 60, 'RIGHT']]
        self.direction = 'RIGHT'
        self.turn = self.direction

    def ChangeDirection(self, direction):

        if direction == 'RIGHT' and not self.direction == 'LEFT':
            self.direction = direction
        if direction == 'LEFT' and not self.direction == 'RIGHT':
            self.direction = direction
        if direction == 'DOWN' and not self.direction == 'UP':
            self.direction = direction
        if direction == 'UP' and not self.direction == 'DOWN':
            self.direction = direction

    def moveSnake(self, foodposition):
        if self.direction == 'RIGHT':
            self.position[0] += 20
        elif self.direction == 'LEFT':
            self.position[0] -= 20
        elif self.direction == 'UP':
            self.position[1] -= 20
        elif self.direction == 'DOWN':
            self.position[1] += 20
        self.body.insert(0, [self.position[0], self.position[1], self.direction])
        if self.position == foodposition:
            return 1
        else:
            self.body.pop()
            return 0

    def checkCollision(self):

        if self.position[0] > 380 or self.position[0] < 0 or self.position[1] > 380 or self.position[1] < 0:
            return 1

        for bodyPart in self.body[1:]:
            if self.position[0] == bodyPart[0] and self.position[1] == bodyPart[1]:
                return 1

        return 0

    def getHeadPosition(self):
        return self.position

    def getBody(self):
        return self.body

    def getDir(self):
        return self.direction


class Food():
    def __init__(self):
        self.position = [random.randrange(1, 20) * 20, random.randrange(1, 20) * 20]
        self.isFoodOnScreen = True

    def generateFood(self):
        if self.isFoodOnScreen == False:
            self.position = [random.randrange(1, 20) * 20, random.randrange(1, 20) * 20]
            self.isFoodOnScreen = True
        return self.position

    def isFoodEaten(self, boolval):
        self.isFoodOnScreen = boolval

    def getfoodpos(self):
        return self.position


gameWindow = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Beware Of Snakes')
speed = pygame.time.Clock()

score = 0

snake = snakeBody()
food = Food()


def gameOver():
    pygame.quit()
    sys.exit()


changedirto = ''
headorientation = ''


def updateCSV():
    with open('Snake_DS.csv', 'a') as snakeDB:
        snakeDB.write('\n{},{},{},{},{},{}'.format(food.position[0], food.position[1], snake.getHeadPosition()[0], snake.getHeadPosition()[1], snake.direction, changedirto))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.ChangeDirection('RIGHT')
                changedirto = 'RIGHT'
                headorientation = 'RIGHT'
            if event.key == pygame.K_LEFT:
                snake.ChangeDirection('LEFT')
                changedirto = 'LEFT'
                headorientation = 'LEFT'
            if event.key == pygame.K_UP:
                snake.ChangeDirection('UP')
                changedirto = 'UP'
                headorientation = 'UP'
            if event.key == pygame.K_DOWN:
                snake.ChangeDirection('DOWN')
                changedirto = 'DOWN'
                headorientation = 'DOWN'

    foodposition = food.generateFood()
    if snake.moveSnake(foodposition) == 1:
        score += 1
        food.isFoodEaten(False)

    gameWindow.fill(pygame.Color(255, 255, 255))

    FOOD = pygame.image.load('food.png')
    H_U = pygame.image.load('h_U.png')
    H_D = pygame.image.load('h_D.png')
    H_R = pygame.image.load('h_R.png')
    H_L = pygame.image.load('h_L.png')
    B_V = pygame.image.load('b_V.png')
    B_H = pygame.image.load('b_H.png')
    T_U = pygame.image.load('t_U.png')
    T_D = pygame.image.load('t_D.png')
    T_R = pygame.image.load('t_R.png')
    T_L = pygame.image.load('t_L.png')
    UR_LD = pygame.image.load('be_UR_LD.png')
    UL_RD = pygame.image.load('be_UL_RD.png')
    RU_DL = pygame.image.load('be_RU_DL.png')
    DR_LU = pygame.image.load('be_DR_LU.png')

    counter = 0

    gameWindow.blit(FOOD, (foodposition[0], foodposition[1]))

    for pos in snake.getBody():
        if counter == 0:
            if snake.direction == 'RIGHT':
                gameWindow.blit(H_R, (pos[0], pos[1]))
            if snake.direction == 'LEFT':
                gameWindow.blit(H_L, (pos[0], pos[1]))
            if snake.direction == 'UP':
                gameWindow.blit(H_U, (pos[0], pos[1]))
            if snake.direction == 'DOWN':
                gameWindow.blit(H_D, (pos[0], pos[1]))
        elif counter < len(snake.body)-1:
            if pos[2] != snake.body[counter-1][2]:
                if pos[2] == 'LEFT' and snake.body[counter-1][2] == 'DOWN' or pos[2] == 'UP' and snake.body[counter-1][2] == 'RIGHT':
                    gameWindow.blit(UR_LD, (pos[0], pos[1]))
                elif pos[2] == 'UP' and snake.body[counter-1][2] == 'LEFT' or pos[2] == 'RIGHT' and snake.body[counter-1][2] == 'DOWN':
                    gameWindow.blit(UL_RD, (pos[0], pos[1]))
                elif pos[2] == 'LEFT' and snake.body[counter-1][2] == 'UP' or pos[2] == 'DOWN' and snake.body[counter-1][2] == 'RIGHT':
                    gameWindow.blit(DR_LU, (pos[0], pos[1]))
                elif pos[2] == 'RIGHT' and snake.body[counter-1][2] == 'UP' or pos[2] == 'DOWN' and snake.body[counter-1][2] == 'LEFT':
                    gameWindow.blit(RU_DL, (pos[0], pos[1]))
            else:
                if pos[2] == 'RIGHT' or pos[2] == 'LEFT':
                    gameWindow.blit(B_H, (pos[0], pos[1]))
                if pos[2] == 'UP' or pos[2] == 'DOWN':
                    gameWindow.blit(B_V, (pos[0], pos[1]))
        elif counter == len(snake.body)-1:
            if pos[2] != snake.body[counter-1][2]:
                if snake.body[counter-1][2] == 'RIGHT':
                    gameWindow.blit(T_L, (pos[0], pos[1]))
                if snake.body[counter-1][2] == 'LEFT':
                    gameWindow.blit(T_R, (pos[0], pos[1]))
                if snake.body[counter-1][2] == 'DOWN':
                    gameWindow.blit(T_U, (pos[0], pos[1]))
                if snake.body[counter-1][2] == 'UP':
                    gameWindow.blit(T_D, (pos[0], pos[1]))
            else:
                if pos[2] == 'RIGHT':
                    gameWindow.blit(T_L, (pos[0], pos[1]))
                if pos[2] == 'LEFT':
                    gameWindow.blit(T_R, (pos[0], pos[1]))
                if pos[2] == 'DOWN':
                    gameWindow.blit(T_U, (pos[0], pos[1]))
                if pos[2] == 'UP':
                    gameWindow.blit(T_D, (pos[0], pos[1]))

        counter += 1


    if snake.checkCollision() == 1:
        gameOver()


    updateCSV()
    pygame.display.set_caption('Score '+str(score))
    pygame.display.flip()

    speed.tick(10)
