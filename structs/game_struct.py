import queue

from constants.canvas import JUMP

QUEUE_SIZE = 300

UP    = 0
RIGHT = 1
DOWN  = 2
LEFT  = 3

class Game_conf:

    def __init__(self):
        self._pos_x = 0
        self._pos_y = 0
        self._pontuacao = 0
        self._atual_direction = RIGHT
        self._snake_body = queue.Queue(QUEUE_SIZE)
        self._food = {'x': -1, 'y': -1, 'o': None}

    def x(self):
        return self._pos_x

    def y(self):
        return self._pos_y

    """ Snake Actions """
    def dec_x(self):
        self._pos_x -= JUMP
        self._atual_direction = LEFT

    def dec_y(self):
        self._pos_y -= JUMP
        self._atual_direction = UP

    def inc_x(self):
        self._pos_x += JUMP
        self._atual_direction = RIGHT

    def inc_y(self):
        self._pos_y += JUMP
        self._atual_direction = DOWN

    def get_direction(self):
        return self._atual_direction

    """ Pontuation """
    def inc_pont(self):
        self._pontuacao += 1
    
    def refresh_pont(self):
        self._pontuacao = 0

    def get_pont(self):
        return self._pontuacao
        
    """ Snake Body """
    def add_body_part(self, part):
        self._snake_body.put(part)

    def rem_body_part(self):
        return self._snake_body.get()

    def get_snake_body(self):
        return self._snake_body
    """ Food methods """
    def add_food(self, x, y, content):
        self._food['x'] = x
        self._food['y'] = y
        self._food['o'] = content
    
    def rem_food(self):
        self._food = {'x': -1, 'y': -1, 'o': None}
    
    def get_food(self):
        return self._food