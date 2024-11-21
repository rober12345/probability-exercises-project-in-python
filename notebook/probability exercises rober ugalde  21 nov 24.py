# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:38:25 2024

@author: rober ugalde


Probability exercises
Exercise 1
Two dices are thrown once and the total score is observed. Use a simulation to find the estimated probability that the total score is even or greater than 7. A simulation is a repetition of the same experiment multiple times to observe its behavior:

Run the experiment 1000 times (roll 2 dice 1000 times, and sum the number of both dices).
Keep track of the number of times that the sum was either greater than 7 or an even number.
Divide the number from step 2 by the number of iterations (1000).
"""

import random

# Simulation parameters
iterations = 1000
success_count = 0

# Run the simulation
for _ in range(iterations):
    dice1 = random.randint(1, 6)  # Roll the first die
    dice2 = random.randint(1, 6)  # Roll the second die
    total = dice1 + dice2         # Calculate the total score

    # Check if the total is even or greater than 7
    if total % 2 == 0 or total > 7:
        success_count += 1

# Calculate the estimated probability
estimated_probability = success_count / iterations

# Print the result
print(f"Estimated Probability: {estimated_probability:.4f}")



"""
Exercise 2
A box contains 10 white balls, 20 red balls and 30 green balls. If we take 5 balls from the box with replacement (we take the ball, observe what color it is and put it back into the box). We want to know the probability of:

Take 3 white and 2 red.
Take all of the same color.
Run the experiment 1000 times and calculate the above probabilities.

"""


import random

# Ball probabilities
white_prob = 10 / 60
red_prob = 20 / 60
green_prob = 30 / 60

# Simulation parameters
iterations = 1000
white_and_red_count = 0
same_color_count = 0

# Run the simulation
for _ in range(iterations):
    draw = [random.choices(['white', 'red', 'green'], weights=[white_prob, red_prob, green_prob])[0] for _ in range(5)]

    # Check if 3 white and 2 red were drawn
    if draw.count('white') == 3 and draw.count('red') == 2:
        white_and_red_count += 1

    # Check if all balls are of the same color
    if len(set(draw)) == 1:
        same_color_count += 1

# Calculate probabilities
prob_white_and_red = white_and_red_count / iterations
prob_same_color = same_color_count / iterations

# Print results
print(f"Probability of 3 white and 2 red: {prob_white_and_red:.4f}")
print(f"Probability of all balls being the same color: {prob_same_color:.4f}")



xxxxx
"""
Exercise 2
A box contains 10 white balls, 20 red balls and 30 green balls. If we take 5 balls from the box with replacement (we take the ball, observe what color it is and put it back into the box). We want to know the probability of:

Take 3 white and 2 red.
Take all of the same color.
Run the experiment 1000 times and calculate the above probabilities.

ball_box = {}

# Create the box of balls
for i in range(60):
    if i < 10:
        ball_box[i] = "White"
    elif (i > 9) and (i < 30):
        ball_box[i] = "Red"
    else:
        ball_box[i] = "Green"

print(ball_box)
            
# TODO
{0: 'White', 1: 'White', 2: 'White', 3: 'White', 4: 'White', 5: 'White', 6: 'White', 7: 'White', 8: 'White', 9: 'White', 10: 'Red', 11: 'Red', 12: 'Red', 13: 'Red', 14: 'Red', 15: 'Red', 16: 'Red', 17: 'Red', 18: 'Red', 19: 'Red', 20: 'Red', 21: 'Red', 22: 'Red', 23: 'Red', 24: 'Red', 25: 'Red', 26: 'Red', 27: 'Red', 28: 'Red', 29: 'Red', 30: 'Green', 31: 'Green', 32: 'Green', 33: 'Green', 34: 'Green', 35: 'Green', 36: 'Green', 37: 'Green', 38: 'Green', 39: 'Green', 40: 'Green', 41: 'Green', 42: 'Green', 43: 'Green', 44: 'Green', 45: 'Green', 46: 'Green', 47: 'Green', 48: 'Green', 49: 'Green', 50: 'Green', 51: 'Green', 52: 'Green', 53: 'Green', 54: 'Green', 55: 'Green', 56: 'Green', 57: 'Green', 58: 'Green', 59: 'Green'}


xxxx

"""

import random

# Create the box of balls
ball_box = {i: "White" if i < 10 else "Red" if i < 30 else "Green" for i in range(60)}

# Parameters for simulation
iterations = 1000
three_white_two_red_count = 0
same_color_count = 0

# Run the simulation
for _ in range(iterations):
    # Randomly draw 5 balls with replacement
    draws = [ball_box[random.randint(0, 59)] for _ in range(5)]
    
    # Check if 3 white and 2 red were drawn
    if draws.count("White") == 3 and draws.count("Red") == 2:
        three_white_two_red_count += 1
    
    # Check if all balls are of the same color
    if len(set(draws)) == 1:
        same_color_count += 1

# Calculate probabilities
prob_three_white_two_red = three_white_two_red_count / iterations
prob_same_color = same_color_count / iterations

# Print results
print(f"Probability of 3 white and 2 red: {prob_three_white_two_red:.4f}")
print(f"Probability of all balls being the same color: {prob_same_color:.4f}")
