fish = [5,1,4,1,5,1,1,5,4,4,4,4,5,1,2,2,1,3,4,1,1,5,1,5,2,2,2,2,1,4,2,4,3,3,3,3,1,1,1,4,3,4,3,1,2,1,5,1,1,4,3,3,1,5,3,4,1,1,3,5,2,4,1,5,3,3,5,4,2,2,3,2,1,1,4,1,2,4,4,2,1,4,3,3,4,4,5,3,4,5,1,1,3,2,5,1,5,1,1,5,2,1,1,4,3,2,5,2,1,1,4,1,5,5,3,4,1,5,4,5,3,1,1,1,4,5,3,1,1,1,5,3,3,5,1,4,1,1,3,2,4,1,3,1,4,5,5,1,4,4,4,2,2,5,5,5,5,5,1,2,3,1,1,2,2,2,2,4,4,1,5,4,5,2,1,2,5,4,4,3,2,1,5,1,4,5,1,4,3,4,1,3,1,5,5,3,1,1,5,1,1,1,2,1,2,2,1,4,3,2,4,4,4,3,1,1,1,5,5,5,3,2,5,2,1,1,5,4,1,2,1,1,1,1,1,2,1,1,4,2,1,3,4,2,3,1,2,2,3,3,4,3,5,4,1,3,1,1,1,2,5,2,4,5,2,3,3,2,1,2,1,1,2,5,3,1,5,2,2,5,1,3,3,2,5,1,3,1,1,3,1,1,2,2,2,3,1,1,4,2]
day = 0

# set up groups for fish with 8 days, 7 days, and so on
fish_bins = [0] * 9

# initialize bins from starting point
for f in fish:
    fish_bins[f] += 1

# model growth based on starting point
while day < 256:
    day += 1
    spawners = fish_bins.pop(0)
    fish_bins[6] += spawners
    fish_bins.append(spawners)

print(f'Bin sum: {sum(fish_bins)}')

""" 
while day < 80:
    new_fish = []
    day += 1

    for n in range(len(fish)):
        if fish[n] == 0:
            fish[n] = 6
            new_fish.append(8)
        else:
            fish[n] -= 1
    fish.extend(new_fish)

print(len(fish)) """