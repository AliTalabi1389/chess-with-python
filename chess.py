import pgzrun
import pygame
import sys
from settings import *
from ctypes import windll
from tkinter import Tk
from game import *

game = Game()

root = Tk()
half_screen_width = root.winfo_screenwidth() // 4
half_screen_height = root.winfo_screenheight() // 4
mod = sys.modules['__main__']
hwnd = pygame.display.get_wm_info()['window']
windll.user32.MoveWindow(hwnd, half_screen_width, 0, HEIGHT, False)

def draw():
    mod.screen.blit("board", (0, 0))
    game.draw()

def update():
    game.update()

def on_mouse_down(pos):
    game.check_mouse_down(pos)

pgzrun.go()