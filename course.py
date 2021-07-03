from typing import List
class Course:
    def __init__(self, name: str = 'Unknown Golf Course', parList: List[int] = None):
        self.name = name
        self.parList = parList if parList else []
        self.courseScore = sum(self.parList)

    def getParsAsString(self):
        return str(self.parList)
