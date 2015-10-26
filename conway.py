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
white = Color(0, 0)
noline = LineStyle(0, black)

class Conway(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        Cell((0,100))
        Cell((10,100))
        Cell((20,100))
        #initiate with white?
        #for x in range(0,100,11):
            #for y in range(0,100,11):
                #Cell((x,y))
        
    def step(self):
        for Cell in self.getSpritesbyClass():
            Cell.destroyornah()
            
    #def mouseClick(event):
        #Cell.x=event.x
        #Cell.y=event.y
     
    #def initiate("""change the attributes"""self, event):
        #self.color = black
        
class Cell(Sprite):
    pixel = RectangleAsset(10,10,noline,black)
    #nopixel = RectangleAsset(5,5,noline,white)

    def __init__(self, position):
        super().__init__(Cell.pixel, position)
        #Conway.listenKeyEvent("keydown", "space", self.#initiate cell)
    
    #def destroyornah(self):
        
#myapp.listenMouseEvent('click',mouseClick)
myapp = Conway(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()