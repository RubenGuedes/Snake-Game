# Standard lib
import copy
import random
from time import sleep
from tkinter import Canvas, Frame, Label, Tk, messagebox

# Own lib
from constants.canvas import JUMP, MAXSIDE_CANVAS, WIDTH_CANVAS_
from constants.colors import DARKER_BLUE, LIGHTER_BLUE, V_BLUE
from constants.percent import PR_0, PR_5, PR_20, PR_100
from constants.str_font import FONT_20, GAME_TITLE, PONTUATION
from constants.window_dim import (GEOMETRY_SIZE, MAX_HEIGHT, MAX_WIDTH_,
                                  MIN_HEIGHT, MIN_WIDTH_)
from structs.game_struct import DOWN, RIGHT, UP, Game_conf
