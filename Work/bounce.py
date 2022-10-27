# bounce.py
#
# Exercise 1.5

"""
A rubber ball is dropped from a height of 100 meters and each time it hits the ground, it bounces back up to 3/5 the height it fell. 
Write a program bounce.py that prints a table 
showing the height of the first 10 bounces.
"""

height = 100 
num_bounce = 1

while num_bounce <= 10:
    height = height * (3/5)
    print(num_bounce, round(height, 4))
    num_bounce += 1

print('Number of Bounces: ', num_bounce)
print('Height bounced: ', height)