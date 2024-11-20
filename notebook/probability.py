# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 07:40:20 2024

@author: rober ugalde
"""

# Given probabilities
P_A = 0.3          # Probability of choosing a red marble
P_not_A = 0.7      # Probability of choosing a blue marble
P_B_given_A = 0.5  # Probability of stripes given the marble is red
P_B_given_not_A = 0.1  # Probability of stripes given the marble is blue

# Total probability of B (the marble has stripes)
P_B = (P_B_given_A * P_A) + (P_B_given_not_A * P_not_A)

# Apply Bayes' theorem to find P(A | B)
P_A_given_B = (P_B_given_A * P_A) / P_B

# Print the result
print(f"The probability that the marble is red given that it has stripes is: {P_A_given_B:.2f}")
