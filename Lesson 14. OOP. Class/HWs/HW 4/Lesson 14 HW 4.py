#(Optional) Create a Robot class with the following attributes:
# orientation (left, right, up, down),
# position_x, position_y.
# The Robot class should have the following methods:
# move, turn, and display_position.
# The move method should take a number of steps
# and move the robot in the direction it is currently facing.
# The turn method should take a direction (left or right)
# and turn the robot in that direction.
# The display_position method should print the current position of the robot.

class Robot:
    def __init__(self, orientation, position_x=0, position_y=0):
        self.orientation = orientation
        self.position_x = position_x
        self.position_y = position_y

    def move(self, steps: int):
        if self.orientation == "Right":
            self.position_x += steps
        elif self.orientation == "Left":
            self.position_x -= steps
        elif self.orientation == "Up":
            self.position_y += steps
        elif self.orientation == "Down":
            self.position_y -= steps

    def turn(self, direction: str):
        if direction == "Right":
            if self.orientation == "Up":
                self.orientation = "Right"
            elif self.orientation == "Right":
                self.orientation = "Down"
            elif self.orientation == "Down":
                self.orientation = "Left"
            elif self.orientation == "Left":
                self.orientation = "Up"
        elif direction == "Left":
            if self.orientation == "Right":
                self.orientation = "Up"
            elif self.orientation == "Down":
                self.orientation = "Right"
            elif self.orientation == "Left":
                self.orientation = "Down"
            elif self.orientation == "Up":
                self.orientation = "Left"

    def display_position(self):
        print(f"Your position is: x: {self.position_x}, y: {self.position_y} and your orientation is: {self.orientation}")


robot = Robot("Up")
robot.move(1)
robot.display_position()

robot.turn("Right")
robot.move(2)
robot.display_position()

