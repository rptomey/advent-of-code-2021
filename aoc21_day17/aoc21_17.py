starting_x = 0
starting_y = 0

target_x_min = 56
target_x_max = 76

target_y_min = -162
target_y_max = -134

target_x = list(range(target_x_min, target_x_max+1))
target_y = list(range(target_y_min, target_y_max+1))

# figure out what the lowest possible x velocity can be to not run out of energy before the target
minimum_x_velocity = 0
snowball_sum = 0

while snowball_sum < target_x_min:
    minimum_x_velocity += 1
    snowball_sum += minimum_x_velocity

# set the variables for my answers
valid_velocities = []
maximum_valid_height = 0

# check all of the reasonable velocities to see if they hit the area
for initial_x in range(minimum_x_velocity, target_x_max+2):
    for initial_y in range(target_y_min, abs(target_y_min)+1):
        # make sure current values don't overwrite the original values
        current_x = starting_x
        current_y = starting_y
        x_velocity = initial_x
        y_velocity = initial_y

        # keep track of each arc's max height
        max_height = 0

        # stop tracking shots as soon as they go beyond the point of being able to hit the target
        while current_x <= target_x_max and current_y >= target_y_min - 1:
            # update based on the step instructions
            current_x += x_velocity
            current_y += y_velocity
            if x_velocity > 0:
                x_velocity -= 1
            elif x_velocity < 0:
                x_velocity += 1
            y_velocity -= 1

            # get the peak of the arc
            if current_y > max_height:
                max_height = current_y

            # as soon as one hits the target, do stuff
            if current_x in target_x and current_y in target_y:
                # add the initial velocity to our list of valid velocities
                valid_velocities.append([initial_x,initial_y])
                # update so that we can find the highest possible arc on a valid shot
                if max_height > maximum_valid_height:
                    maximum_valid_height = max_height
                # move on to test the next shot
                break

print(maximum_valid_height)
print(len(valid_velocities))