#==============================================================================
# Simulation: Estimating Pi by dropping needles on a hardwood floor
# Related article: https://medium.com/@andrew.chamberlain/a-sewing-circle-method-for-estimating-pi-5a7ec443863b
# by Andrew Chamberlain, Ph.D.
# achamberlain.com
#==============================================================================

import random
import math

num_needles = 1000000  # Number of needles to drop
needle_length = 1.0    # Length of each needle
line_distance = 2.0    # Distance between parallel lines

# Counter for needles crossing a line on the floor
needles_crossing = 0

# Simulate dropping needles
for _ in range(num_needles):
    # Generate random position for the center of the needle
    y_center = random.uniform(0, line_distance)
    
    # Generate random angle in radians (0 to π)
    angle = random.uniform(0, math.pi)
    
    # Calculate the distance from the center of the needle to the closest line
    distance_to_closest_line = min(y_center, line_distance - y_center)
    
    # Calculate the maximum distance from the center to a line
    # that would still allow the needle to cross the line
    max_crossing_distance = (needle_length / 2) * math.sin(angle)
    
    # Check if the needle crosses a line
    if distance_to_closest_line <= max_crossing_distance:
        needles_crossing += 1

pi_estimate = (2 * needle_length * num_needles) / (line_distance * needles_crossing)

# Print results
print(f"Number of needles dropped: {num_needles}")
print(f"Number of needles crossing a line: {needles_crossing}")
print(f"Probability of crossing: {needles_crossing / num_needles}")
print(f"Estimate of Pi: {pi_estimate}")
print(f"Actual value of Pi: {math.pi}")
print(f"Difference: {abs(pi_estimate - math.pi)}")
