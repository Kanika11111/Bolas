# ball.py

class Ball:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def change_color(self, new_color):
        self.color = new_color

    def __str__(self):
        return f"Ball(radius={self.radius}, color='{self.color}')"
