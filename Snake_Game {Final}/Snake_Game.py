# -*- coding: utf-8 -*-

import pygame
import random
import time
import numpy as np
import sys

########################################################################################################################

class snakeBody():

    def __init__(self):

        self.position = [120, 60]
        self.body = [[120, 60, 'RIGHT'], [80, 60, 'RIGHT'], [60, 60, 'RIGHT']]
        self.direction = 'RIGHT'
        self.turn = self.direction

    def ChangeDirection(self, direction):

        if (direction == 'RIGHT' and not self.direction == 'LEFT'):
            self.direction = direction
        if (direction == 'LEFT' and not self.direction == 'RIGHT'):
            self.direction = direction
        if (direction == 'DOWN' and not self.direction == 'UP'):
            self.direction = direction
        if (direction == 'UP' and not self.direction == 'DOWN'):
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

        # inserting at the 0th position.
        self.body.insert(0, [self.position[0], self.position[1], self.direction])

        if (self.position == foodposition):
            return 1
        else:
            self.body.pop()
            return 0

    def checkCollision(self):

        # collision in x axis boundary.
        if (self.position[0] > 380 or self.position[0] < 0 ):
            #crashsound.play()
            return 1

        # collision in y axis boundary.
        elif (self.position[1] > 380 or self.position[1] < 0):
            #crashsound.play()
            return 1

        # Here we want to check that if the body is collided with the head itself
        # that's why we have excluded the head and started from [1:].
        for bodyPart in self.body[1:]:
            if self.position[0] == bodyPart[0] and self.position[1] == bodyPart[1]:
                #eatsound.play()
                return 1

        return 0

    def getHeadPosition(self):
        return self.position

    def getBody(self):
        return self.body

########################################################################################################################

class Food():
    def __init__(self):
        self.position = [random.randrange(1, 20)*20, random.randrange(1, 20)*20]
        self.isFoodOnScreen = True
        
    def generateFood(self):
        if self.isFoodOnScreen == False:
            self.position = [random.randrange(1, 20)*20, random.randrange(1, 20)*20]
            self.isFoodOnScreen = True
        return self.position

    def isFoodEaten(self, boolval):
        self.isFoodOnScreen = boolval

########################################################################################################################

def gameOver():

    pygame.quit()
    sys.exit()


def gameContinue():

    gameWindow.blit(game_over, (25, 100))
    pygame.display.flip()

    time.sleep(3)

    snake.position = [120, 60]
    snake.body = [[120, 60, 'RIGHT'], [80, 60, 'RIGHT'], [60, 60, 'RIGHT']]
    snake.direction = 'RIGHT'
    snake.turn = snake.direction


def updateCSV(Left_B,Front_B,Right_B,Cosine_Angle,Collision,Head_x,Head_y,Food_x,Food_y,Sugg_Direction):
    with open('Snake_Dataset.csv', 'a') as snakeDB:
        snakeDB.write('\n{},{},{},{},{},{},{},{},{},{}'.format(Left_B,Front_B,Right_B,Cosine_Angle,Collision,Head_x,Head_y,Food_x,Food_y,Sugg_Direction))


def angleCal(x, y):

    # divide by error generated in this case so handling with if condition.
    if(np.dot(x, y)== 0.0 and (np.linalg.norm(x) * np.linalg.norm(y))==0.0 ):
        return (0.0)

    else:
        cosine_angle = np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))
        a = np.arccos(cosine_angle)

        angle = np.degrees(a)

        angle = round(angle, 2)
        return(angle)

def getSuggestion(angle):

    if(angle >= 0.0 and angle <= 90.0):
        return (1)

    if(angle >=91.0 and angle <= 180.0):
        return (0)

    return(1)



gameWindow = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Snake Game")

# setting the icon in the windows.
icon = pygame.image.load('Snake_Game.jpg')
pygame.display.set_icon(icon)

#eatsound = pygame.mixer.Sound('snakeeat.wav')
#crashsound = pygame.mixer.Sound('snakecrash.wav')

game_over = pygame.image.load('go.png')

snake_food = pygame.image.load('food.png')
bg_image = pygame.image.load('bg.png')

Head_Up = pygame.image.load('h_U.png')
Head_Do = pygame.image.load('h_D.png')
Head_Ri = pygame.image.load('h_R.png')
Head_Le = pygame.image.load('h_L.png')

Tail_Up = pygame.image.load('t_U.png')
Tail_Do = pygame.image.load('t_D.png')
Tail_Ri = pygame.image.load('t_R.png')
Tail_Le = pygame.image.load('t_L.png')

Bend_RL = pygame.image.load('b_RL.png')
Bend_UD = pygame.image.load('b_DU.png')

Bend_1 = pygame.image.load('be_UL.png')
Bend_2 = pygame.image.load('be_UR.png')
Bend_3 = pygame.image.load('be_DR.png')
Bend_4 = pygame.image.load('be_DL.png')

speed = pygame.time.Clock()


snake = snakeBody()
food = Food()


L = 0
F = 0
R = 0
D = 0
C = 0
N = 0

score = 0


def gameRun():


    # adding background image to the game window.
    gameWindow.blit(bg_image, (0, 0))

    # To display the score in the title bar.
    pygame.display.set_caption("Snake Game | Your Score : " + str(score))


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            gameOver()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.ChangeDirection('RIGHT')
            if event.key == pygame.K_LEFT:
                snake.ChangeDirection('LEFT')
            if event.key == pygame.K_UP:
                snake.ChangeDirection('UP')
            if event.key == pygame.K_DOWN:
                snake.ChangeDirection('DOWN')

    foodposition = food.generateFood()

    if snake.moveSnake(foodposition) == 1:
        #score += 1

        food.isFoodEaten(False)

    counter = 0

###################################################################################################################################

    for pos in snake.getBody():

        if(counter == 0):

            L = 0
            R = 0
            F = 0

            if (snake.direction == 'RIGHT'):
                gameWindow.blit(Head_Ri, (pos[0], pos[1]))

                # finding the cosine angle.
                x = np.array(foodposition) - np.array(snake.body[0][0:2])
                y = np.array(snake.body[0][0:2]) - np.array(snake.body[1][0:2])
                N = angleCal(x, y)

                # generating the suggested direction.
                C = getSuggestion(N)

                # Direction in which snake move for RIGHT it is 1.
                D = '1'

                # collision along th wall only.
                if(snake.body[0][1] == 0):
                    L = 1
                if(snake.body[0][0] == 380):
                    F = 1
                if(snake.body[0][1] == 380 ):
                    R = 1

                # collision with the body parts.
                for i in range(0, len(snake.body)):

                    if(snake.body[0][0] == snake.body[i][0]):
                        if (snake.body[0][1] == snake.body[i][1] + 20):
                            L = 1

                    if (snake.body[0][0] == snake.body[i][0]):
                        if (snake.body[0][1] == snake.body[i][1] - 20):
                            R = 1

                    if (snake.body[0][1] == snake.body[i][1]):
                        if (snake.body[0][0] == snake.body[i][0] - 20):
                            F = 1


            if (snake.direction == 'LEFT'):
                gameWindow.blit(Head_Le, (pos[0], pos[1]))

                x = np.array(foodposition) - np.array(snake.body[0][0:2])
                y = np.array(snake.body[0][0:2]) - np.array(snake.body[1][0:2])

                N = angleCal(x, y)
                C = getSuggestion(N)

                D = '2'

                # collision along th wall only.
                if (snake.body[0][1] == 380):
                    L = 1
                if (snake.body[0][0] == 0):
                    F = 1
                if (snake.body[0][1] == 0):
                    R = 1

               # collision with the body parts.
                for i in range(0, len(snake.body)):

                    if(snake.body[0][0] == snake.body[i][0]):
                        if (snake.body[0][1] == snake.body[i][1] + 20):
                            R = 1

                    if (snake.body[0][0] == snake.body[i][0]):
                        if (snake.body[0][1] == snake.body[i][1] - 20):
                            L = 1

                    if (snake.body[0][1] == snake.body[i][1]):
                        if (snake.body[0][0] == snake.body[i][0] + 20):
                            F = 1



            if (snake.direction == 'UP'):
                gameWindow.blit(Head_Up, (pos[0], pos[1]))

                x = np.array(foodposition) - np.array(snake.body[0][0:2])
                y = np.array(snake.body[0][0:2]) - np.array(snake.body[1][0:2])

                N = angleCal(x, y)
                C = getSuggestion(N)

                D = '3'

                # collision along th wall only.
                if (snake.body[0][0] == 0):
                    L = 1
                if (snake.body[0][1] == 0):
                    F = 1
                if (snake.body[0][0] == 380):
                    R = 1

               # collision with the body parts.
                for i in range(0, len(snake.body)):

                    if(snake.body[0][1] == snake.body[i][1]):
                        if (snake.body[0][0] == snake.body[i][0] + 20):
                            L = 1

                    if (snake.body[0][1] == snake.body[i][1]):
                        if (snake.body[0][0] == snake.body[i][0] - 20):
                            R = 1

                    if (snake.body[0][0] == snake.body[i][0]):
                        if (snake.body[0][1] == snake.body[i][1] + 20):
                            F = 1



            if (snake.direction == 'DOWN'):
                gameWindow.blit(Head_Do, (pos[0], pos[1]))

                x = np.array(foodposition) - np.array(snake.body[0][0:2])
                y = np.array(snake.body[0][0:2]) - np.array(snake.body[1][0:2])

                N = angleCal(x, y)
                C = getSuggestion(N)

                D = '4'

                # collision along th wall only.
                if (snake.body[0][0] == 380):
                    L = 1
                if (snake.body[0][1] == 380):
                    F = 1
                if (snake.body[0][0] == 0):
                    R = 1

               # collision with the body parts.
                for i in range(0, len(snake.body)):

                    if(snake.body[0][1] == snake.body[i][1]):
                        if (snake.body[0][0] == snake.body[i][0] + 20):
                            R = 1

                    if (snake.body[0][1] == snake.body[i][1]):
                        if (snake.body[0][0] == snake.body[i][0] - 20):
                            L = 1

                    if (snake.body[0][0] == snake.body[i][0]):
                        if (snake.body[0][1] == snake.body[i][1] - 20):
                            F = 1


            if snake.checkCollision() == 1:
                C = -1

            updateCSV(L, F, R, N, C, pos[0], pos[1], foodposition[0], foodposition[1], D)

            print(L, "\t", F, "\t", R, "\t", N, "\t", C, "\t", pos[0], "\t", pos[1], "\t", foodposition[0], "\t", foodposition[1], "\t", D)
###################################################################################################################################

        elif counter < len(snake.body) - 1:

            if pos[2] != snake.body[counter - 1][2]:

                if pos[2] == 'LEFT' and snake.body[counter - 1][2] == 'DOWN' or pos[2] == 'UP' and snake.body[counter - 1][2] == 'RIGHT':
                    gameWindow.blit(Bend_1, (pos[0], pos[1]))

                elif pos[2] == 'UP' and snake.body[counter - 1][2] == 'LEFT' or pos[2] == 'RIGHT' and snake.body[counter - 1][2] == 'DOWN':
                    gameWindow.blit(Bend_2, (pos[0], pos[1]))

                elif pos[2] == 'LEFT' and snake.body[counter - 1][2] == 'UP' or pos[2] == 'DOWN' and snake.body[counter - 1][2] == 'RIGHT':
                    gameWindow.blit(Bend_4, (pos[0], pos[1]))

                elif pos[2] == 'RIGHT' and snake.body[counter - 1][2] == 'UP' or pos[2] == 'DOWN' and snake.body[counter - 1][2] == 'LEFT':
                    gameWindow.blit(Bend_3, (pos[0], pos[1]))

            else:
                if pos[2] == 'RIGHT' or pos[2] == 'LEFT':
                    gameWindow.blit(Bend_RL, (pos[0], pos[1]))

                if pos[2] == 'UP' or pos[2] == 'DOWN':
                    gameWindow.blit(Bend_UD, (pos[0], pos[1]))



        elif counter == len(snake.body) - 1:

            if pos[2] != snake.body[counter - 1][2]:

                if snake.body[counter - 1][2] == 'RIGHT':
                    gameWindow.blit(Tail_Le, (pos[0], pos[1]))

                if snake.body[counter - 1][2] == 'LEFT':
                    gameWindow.blit(Tail_Ri, (pos[0], pos[1]))

                if snake.body[counter - 1][2] == 'DOWN':
                    gameWindow.blit(Tail_Up, (pos[0], pos[1]))

                if snake.body[counter - 1][2] == 'UP':
                    gameWindow.blit(Tail_Do, (pos[0], pos[1]))
            else:

                if pos[2] == 'RIGHT':
                    gameWindow.blit(Tail_Le, (pos[0], pos[1]))

                if pos[2] == 'LEFT':
                    gameWindow.blit(Tail_Ri, (pos[0], pos[1]))

                if pos[2] == 'DOWN':
                    gameWindow.blit(Tail_Up, (pos[0], pos[1]))

                if pos[2] == 'UP':
                    gameWindow.blit(Tail_Do, (pos[0], pos[1]))

        counter += 1

    gameWindow.blit(snake_food, (foodposition[0], foodposition[1]))

    if snake.checkCollision() == 1:
        gameContinue()
        return 0


    # To refresh the display window.
    pygame.display.flip()

    speed.tick(2)

    return 1

while(True):
    while(True):
        if gameRun()==0:
            break

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
