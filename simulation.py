import random
import math

# Number of random points to generate
num_points = 1000000

# Counter for points inside the circle
points_inside_circle = 0

# Generate random points and count those inside the circle
for _ in range(num_points):
    # Generate random coordinates between -1 and 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    
    # Calculate the distance from the origin (0,0)
    distance = math.sqrt(x**2 + y**2)
    
    # Check if the point is inside the circle (radius = 1)
    if distance <= 1:
        points_inside_circle += 1

# Calculate the ratio of points inside the circle to total points
# Since we're using a 2x2 square with a circle of radius 1,
# the ratio of areas is π/4, so we multiply our result by 4
pi_estimate = 4 * points_inside_circle / num_points

# Print results
print(f"Number of points generated: {num_points}")
print(f"Number of points inside the circle: {points_inside_circle}")
print(f"Estimate of Pi: {pi_estimate}")
print(f"Actual value of Pi: {math.pi}")
print(f"Difference: {abs(pi_estimate - math.pi)}")
