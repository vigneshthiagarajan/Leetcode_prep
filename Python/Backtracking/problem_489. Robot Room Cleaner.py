# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

        def return_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtracking_spiral(cell=(0, 0), d=0):
            visited.add(cell)
            robot.clean()

            for i in range(4):
                new_direction = (d + i) % 4
                new_cell = (cell[0] + directions[new_direction]
                            [0], cell[1] + directions[new_direction][1])
                if not new_cell in visited and robot.move():
                    backtracking_spiral(new_cell, new_direction)
                    return_back()

                robot.turnRight()

       # Order is up, right, down, left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        backtracking_spiral()
