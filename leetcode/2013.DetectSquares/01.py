class CountSquares:

    def __init__(self):
        self.point = dict()

    def add(self, point: List[int]) -> None:
        if point[0] not in self.point:
            self.point[point[0]] = dict()
        if point[1] not in self.point[point[0]]:
            self.point[point[0]][point[1]] = 1
        else:
            self.point[point[0]][point[1]] = self.point[point[0]][point[1]] + 1

    def count(self, point: List[int]) -> int:
        counter = 0
        for keyX, keyYItem in self.point.items():
            for keyY, count in keyYItem.items():
                w = abs(point[0] - keyX)
                h = abs(point[1] - keyY)

                if w == h and w != 0:
                    point1Count = 0
                    point2Count = 0
                    if point[1] in self.point[keyX] and point[0] in self.point and keyY in self.point[point[0]]:
                        point1Count = self.point[keyX][point[1]]
                        point2Count = self.point[point[0]][keyY]
                    tempCounter = count * point1Count * point2Count
                    counter = counter + tempCounter

        return counter
