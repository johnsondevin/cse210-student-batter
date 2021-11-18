from batter.game import output_service
from game.action import Action
from output_service import OutputService

class DrawActorsAction(Action):
    def __init__(self, output_service):
        self._output = output_service

    def execute(self, cast):
        self._output.clear_screen()
        for i in cast:
            self._output.draw_actor(i)
        self._output.flush_buffer()