# main.py

from ball import Ball

# Create a small red ball
small_ball = Ball(radius=5, color="red", bounce=0.8, position=(0, 2), weight=2)

# Create a big blue ball
big_ball = Ball(radius=15, color="blue", bounce=0.5, position=(5, 7), weight=7)

# Print their details
print("Small Ball:", small_ball)
print("Big Ball:", big_ball)

# Let's change the color of the small ball
"""
small_ball.change_color("yellow")
print("Small Ball after color change:", small_ball)
"""