"""
conway.py
Author: Adam Pikielny
Credit: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
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
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, black)
bg = Sprite(bg_asset, (0,0))


myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()