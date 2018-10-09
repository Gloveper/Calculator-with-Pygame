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

class Text:

    def __init__(self, surf, text, color = (0,0,0), font="Franklin Gothic Book", size=40, align="left", pos=(0,0)):
        self.text = text
        self.surf = surf
        self.color = color
        self.pos = pos
        self.align = align
        self.font = pygame.font.SysFont(font, size)
        self.textsurf = self.font.render(self.text, True, self.color)
        self.textrect = self.textsurf.get_rect()

    def setText(self, text):
        self.text = text

    def draw(self):
        if self.align == "topleft":
            self.textrect.topleft = (self.pos[0], self.pos[1])
        elif self.align == "center":
            self.textrect.center = (self.pos[0], self.pos[1])
        elif self.align == "topright":
            self.textrect.topright = (self.pos[0], self.pos[1])

        self.surf.blit(self.textsurf, self.textrect)
