# ball.py

class Ball:
    def __init__(self, radius, color, position, bounce, weight):
        self.radius = radius
        self.color = color
        self.position = position
        self.bounce = bounce
        self.min_weight = 0.1
        self.max_weight = 5
        self.weight = self.set_weight(weight)

    def set_weight(self, weight):
        if weight < self.min_weight or weight > self.max_weight:
            print("Invalid weight. Weight should be between", self.min_weight, "and", self.max_weight)
            return None
        return weight
    def change_color(self, new_color):
        self.color = new_color

    def __str__(self):
        return f"Ball(radius={self.radius}, color='{self.color}', position={self.position}, bounce={self.bounce}, weight={self.weight})"
