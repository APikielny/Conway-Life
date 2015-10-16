"""
conway.py
Author: Adam Pikielny
Credit: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
Morgan the legend
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

#need to decide on boundaries: wrap or nah
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Background
black = Color(0, 1)
noline = LineStyle(0, black)

class Conway(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        #initiate with white?
        Cell((100,100))
        Cell((200,100))
        Cell((300,100))
        Cell((100,200))
     
    def initiate("""change the attributes"""self, event):
        self.color = black
        
class Cell(Sprite):
    pixel = RectangleAsset(5,5,noline,black)

    def __init__(self, position):
        super().__init__(Cell.pixel, position)
        Conway.listenKeyEvent("keydown", "space", self.#initiate cell)

myapp = Conway(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()