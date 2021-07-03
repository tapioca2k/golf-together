from typing import List
from course import Course

class Game:
    def __init__(self, name: str = 'Unknown Game', courses: List[Course] = None):
        self.name = name
        self.courses = courses if courses else []
