#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 20:19:20 2018

@author: vivekraj
"""

import pygame
import random
import time
import sys

class snakeBody():
    
    def __init__(self):
        self.position = [100,50];
        self.body = [[100,50],[90,50],[80,50]]
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
            self.position[0] += 10
        elif self.direction == 'LEFT':
            self.position[0] -= 10
        elif self.direction == 'UP':
            self.position[1] -= 10
        elif self.direction == 'DOWN':
            self.position[1] += 10
        self.body.insert(0, list(self.position))
        if (self.position == foodposition):
            return 1
        else:
            self.body.pop()
            return 0
            
    def checkCollision(self):
        
        if (self.position[0] > 600 or self.position[0] < 0 or self.position[1] > 400 or self.position[1] < 0):
            return 1
        
        for bodyPart in self.body[1:]:
            if self.position == bodyPart:
                return 1
        
        return 0

    def getHeadPosition(self):
        return self.position
    
    def getBody(self):
        return self.body
    
class Food():
    def __init__(self):
        self.position = [random.randrange(1,60)*10, random.randrange(1,40)*10]
        self.isFoodOnScreen = True
        
    def generateFood(self):
        if self.isFoodOnScreen == False:
            self.position = [random.randrange(1,60)*10, random.randrange(1,40)*10]
            self.isFoodOnScreen = True
        return self.position
    def isFoodEaten(self, boolval):
        self.isFoodOnScreen = boolval
        
gameWindow = pygame.display.set_mode((600,400))
pygame.display.set_Caption = 'Beware Of Snakes'
speed = pygame.time.Clock()

score = 0

snake = snakeBody()
food = Food()

def gameOver():
    pygame.quit()
    sys.exit()
    
while True:
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
        score += 1
        food.isFoodEaten(False)
    
    gameWindow.fill(pygame.Color(255,255,255))
    
    for pos in snake.getBody():
        pygame.draw.rect(gameWindow, pygame.Color(0,255,0), pygame.Rect(pos[0], pos[1], 10, 10))
    
    pygame.draw.rect(gameWindow, pygame.Color(225,0,0), pygame.Rect(foodposition[0], foodposition[1], 10, 10))
    
    if snake.checkCollision() == 1:
        gameOver()
        
    #pygame.display.set_capiton('Score {}'.format(score))
    pygame.display.flip()
    
    speed.tick(24)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
