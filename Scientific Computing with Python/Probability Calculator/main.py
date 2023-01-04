import copy
import random


class Hat:
    def __init__(self, **balls):
        self.contents = [key for key, value in balls.items() for i in range(value)]

    def draw(self, n):
        if n >= len(self.contents):
            return self.contents
        removed_balls = []
        remove_indices = random.sample(range(len(self.contents)), n)
        for i in remove_indices:
            removed_balls.append(self.contents[i])
        for ball in removed_balls:
            self.contents.remove(ball)
        return removed_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    if num_balls_drawn > len(hat.contents):
        num_balls_drawn = len(hat.contents)
    for i in range(num_experiments):
        # making a deep copy to preserve initial content after drawing
        balls = copy.deepcopy(hat.contents)
        # performing experiment
        drawn_balls = hat.draw(num_balls_drawn)
        found_expected_balls = [False if drawn_balls.count(key) < value else True for key, value in
                                expected_balls.items()]
        # check if all expected balls where found
        if all(found_expected_balls):
            m += 1
        # returning hat contents to its initial state before the draw
        hat.contents = balls
    return m / num_experiments

