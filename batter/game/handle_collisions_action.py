from game import constants
from game.action import Action

class HandleCollisionsAction(Action):
    def execute(self, cast):
        paddle = cast['paddle']
        brick = cast['brick']
        ball = cast['ball'][0]
        if brick.get_position().equals(ball.get_position()):
            #Need function to delete brick
            pass
        if ball.get_position().equals(paddle.get_position() + 1):
            return ball.get_velocity() * -1