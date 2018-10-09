# This is the PyGame-based Basic Calculator program
#
# This calculator can do simple calculation such as plus, minus, multiplied and divided
#
# This project is a part of Software Development Practice 1 course
#
# Developed by Tikamporn nontarom
# Computer Engineering student at KMUTNB
# Student ID: 5901012630067

import pygame
from Button import *
from Text import *

class Main:

    def __init__(self):
        pygame.init()
        self.height = 700
        self.width = 400
        self.color = (255, 255, 255)
        self.run = True
        self.mouse = 0, 0
        self.click = 0, 0
        self.gamedisplay = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Calculator")

    def setBGcolor(self, color):
        self.color = color

    def mousePos(self):
        self.mouse = pygame.mouse.get_pos()

    # def getmousePos(self):
    #     return self.mouse
    def click(self):
        return self.click


    def runGame(self):
        equation = ""
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.click = pygame.mouse.get_pos()

            self.gamedisplay.fill(self.color)
            mouse = pygame.mouse.get_pos()

            buttonText = (("AC", "del", "(" ,")"),
                          ("7", "8", "9", "÷"),
                          ("4", "5", "6", "×"),
                          ("1", "2", "3", "-"),
                          ("0", ".", "=", "+"))

            row = 5
            col = 4
            for i in range(row):
                for j in range(col):
                    xside = self.width//4 * j
                    # rside = self.width//4 * (j+1)
                    yside = self.height//3 + ((self.height//15)*2) * i
                    # bside = self.height//3 + ((self.height//15)*2) * (i + 1)
                    xwidth = self.width//4
                    yheight = ((self.height//15)*2)

                    # if lside < mouse[0] < rside and tside < mouse[1] < bside:
                    #     button = Button(self.gamedisplay, mouse, self.click, color=(124, 185, 232), text=buttonText[i][j])
                    #     button.setRect((lside, tside, xwidth, yheight))
                    #     button.draw()
                    # else :
                    button = Button(self.gamedisplay, mouse, self.click, color=(0, 0, 0), text=buttonText[i][j])
                    button.setRect((xside, yside, xwidth, yheight))
                    button.draw()

                    if button.clicked():
                        s = buttonText[i][j]
                        if s == "=":
                            try:
                                result = str(eval(equation))
                                equation = result
                            except ZeroDivisionError:
                                equation = "Infinity"
                            except TypeError:
                                equation = "Invalid input"
                            except SyntaxError:
                                equation = "Invalid input"
                        elif s == "AC":
                            equation = ""
                        elif s == "del":
                            equation = equation[:-1]
                        elif s == "(":
                            if equation == "0":
                                equation = ""
                            equation += "("
                        elif s == ")":
                            equation += ")"
                        elif s == ".":
                            equation += "."
                        elif s in "0123456789":
                            if equation == "0":
                                equation = ""
                            equation += s
                        elif len(equation) > 0 and equation[-1] not in "+-*/":
                            if s == "+" or s == "-":
                                equation += s
                            elif s == "×":
                                equation += "*"
                            elif s == "÷":
                                equation += "/"

            self.click = 0,0
            if len(equation) < 1:
                equation = "0"

            gamedisplayText = Text(self.gamedisplay , equation, pos=(self.width - 20, self.height//3 - 90), align ="topright", size=60).draw()


            pygame.display.update()

        pygame.quit()
        quit()
game = Main()
game.runGame()
