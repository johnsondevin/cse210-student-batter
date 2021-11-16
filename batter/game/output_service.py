import sys
from game import constants
from asciimatics.widgets import Frame

class OutputService:
    def __init__(self, screen):
        self._screen = screen

    def clear_screen(self):
        self._screen.clear_buffer(7,0,0)
        self._screen.print_at('-' * constants.MAX_X, 0, 0, 7)
        self._screen.print_at('-' * constants.MAX_X, 0, constants.MAX_Y, 7)

    def draw_actor(self, actor):
        pass

    def draw_actors(self, actors):
        pass

    def flush_buffer(self):
        self._screen.refresh()