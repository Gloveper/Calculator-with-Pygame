# This is the PyGame-based Basic Calculator Program
#
# This calculator can do simple calculation such as plus, minus, multiplied and divided
#
# This project is a part of Software Development Practice 1 course
#
# Developed by Tikamporn nontarom
# Computer Engineering student at KMUTNB
# Student ID: 5901012630067

import pygame
from Text import *

class Button:

    def __init__(self, surf, mouse, click, text="button", color=(0, 0, 0), rect=(0, 0, 100, 90)):
        self.surf = surf
        self.mouse = mouse
        self.click = click
        self.text = text
        self.color = color
        self.rect = rect

    def setText(self, text):
        self.text = text

    def setColor(self, color):
        self.color = color

    def setRect(self, rect):
        self.rect = rect

    def setButtonsize(self):
        return (self.rect[2], self.rect[3])

    def draw(self):
        pygame.draw.rect(self.surf, self.color, self.rect, 2)
        Text(self.surf, self.text, pos=(self.rect[0] + self.rect[2] / 2, self.rect[1] + self.rect[3] / 2),
             align="center").draw()
        self.clicked("round")

    def clicked(self, type="normal"):
        lside = self.rect[0]
        rside = lside + self.rect[2]
        tside = self.rect[1]
        bside = tside + self.rect[3]

        if lside < self.mouse[0] < rside and tside < self.mouse[1] < bside:
            self.setColor((124, 185, 232))
            pygame.draw.rect(self.surf, self.color, self.rect, 4)
            if type == "round":
                pygame.draw.rect(self.surf, self.color, self.rect, 2)

            if lside < self.click[0] < rside and tside < self.click[1] < bside:
                return True
        return False


