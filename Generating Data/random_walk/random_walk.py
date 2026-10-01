from random import choice

class RandomWalk():
    """a class to generate random walks"""
    def __init__(self, num_points = 10000):
        """initialize attributes of walk"""
        self.num_points = num_points

        # every walk starts at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """calculate all points in the walk"""
        # keep addings steps until required num_points
        while len(self.x_values) < self.num_points:
            # decide which direction to go and how far to go 
            x_step = self.get_step()
            y_step = self.get_step()
            if x_step == 0 and y_step == 0:
                continue

            # calculate next (x, y) value
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self):
        """get which direction to move in and how far"""
        direction = choice([-1, 1])
        distance = choice([0, 1, 2, 3, 4])
        return direction * distance

