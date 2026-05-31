class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        maxTime = 0.0
        for position, speed in cars:
            totalTime = (target - position) / speed
            if totalTime > maxTime:
                fleets += 1
                maxTime = totalTime

        return fleets
