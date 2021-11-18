from game import constants
from game.action import Action

class ControlActorsAction(Action):
    def __init__(self, input_service):
        self._input_service = input_service

    def execute(self, cast):
        direction = self._input_service.get_direction()
        robot = cast['robot'][0]
        robot.set_velocity(direction)