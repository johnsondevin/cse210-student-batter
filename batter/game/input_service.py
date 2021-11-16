import sys
from game.point import Point
from asciimatics.event import KeyboardEvent

class InputService:
    '''Detects player input. This is used to notice and report any keypresses
    by the user.
    
    Stereotype:
        Service Provider
        
    Attributes:
        _screen (Screen): An Asciimatics screen.
        _keys (list): Points for up, down, left, right.
    '''

    def __init__(self,screen):
        '''The class constructor'''
        self._screen = screen
        self._keys = {}
        self._keys[97] = Point(-1,0)
        self._keys[100] = Point(1,0)

    def get_directions(self):
        '''Obtains desired direction for the player.

        Returns:
            Point: The selected direction.
        '''
        direction = Point(0,0)
        event = self._screen.get_event()
        if isinstance(event, KeyboardEvent):
            if event.key_code == 27:
                sys.exit()
            direction = self._keys.get(event.key_code, Point(0,0))
        return direction