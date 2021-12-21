enhancement_algorithm = '##.......#.####..#..#...##.##...#.####.#.##.######...###...#..#####...###...##.###..#...#....#.#....###.#....##..####...##....###....##.#.###..###.#...####.#....#.#.#.####...#...#.#..#....#######......#..#.###.....#.#...#.....##.##.##..#....##.##.####.#..#..#.#...#..########.##.########....##.#...#...#..#..#.#..#..###..#..##.##.#.#.#.##.##..##....#.##.#.#.##.#..#..####..#...####.##..#.....###...##..##..####..#..#...####.##.##.#.##.#....####..####...#.#.#..#.#.##.##.##.###.#......##.#...#.#.##..##.##..###...'
sample_algorithm = '..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#'
reddit_algorithm = '#.#.#.#.#......#.#.#.#.##..#.##.##..#..##...#.#.#.#...##.##.##.###....#..#...#.#..###.#...#..##.#.###..#..####.###...#.#.#..##..##.##..##..###..#....#.#....#####.#...###...#.#....###...#..##.##..#..#.##..###..#.##.###..#.####...#.##.....#.###...#.##.##.#.#######...#.###..##..##..#.#.#.#####...#....#.....##.#.#...##.######....#..#......#.#.#.#.##...######.#.#####..#####..#.#.#.#.###.#.#....#..##..#..#.#.#..##....##..#.#.......##...#..####.####.#.#..#.###..#...#......###...#...#.##.#.####..#.#....###.####..#.'

images = []
original_image = {}

x_counter = 0
y_counter = 0
with open('aoc21_20_input.txt') as f:
    for line in f:
        for c in line:
            if c == '\n':
                x_counter = 0
                y_counter += 1
            else:
                original_image[f'{x_counter},{y_counter}'] = c
                x_counter += 1

images.append(original_image)

def enhance(image, algorithm, count):
    new_image = {}
    # figure out the current image size
    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0

    for key in image.keys():
        x_pos,y_pos = list(map(int, key.split(',')))
        if x_pos < min_x:
            min_x = x_pos
        if x_pos > max_x:
            max_x = x_pos
        if y_pos < min_y:
            min_y = y_pos
        if y_pos > max_y:
            max_y = y_pos

    # output will need to be one pixel wider each way
    min_x -= 1
    max_x += 1
    min_y -= 1
    max_y += 1

    # go through all existing pixels plus the new border pixels
    for x_pos in range(min_x, max_x+1):
        for y_pos in range(min_y, max_y+1):
            #print(f'checking pixel: {x_pos},{y_pos}')
            # find neighbors and read them to a binary code
            binary = ''
            for y in range(y_pos-1, y_pos+2):
                for x in range(x_pos-1, x_pos+2):
                    #print(f'neighbor {x},{y}')
                    #if x <= 0 or x >= max_x or y <= 0 or y >= max_y:
                    #    binary = binary + '0'
                    try:
                        if image[f'{x},{y}'] == '.':
                            binary = binary + '0'
                        elif image[f'{x},{y}'] == '#':
                            binary = binary + '1'
                    except KeyError:
                        if count % 2 == 0:
                            binary = binary + '0'
                        else:
                            binary = binary + '1'
            #print(f'binary: {binary}')
        
            # convert the binary to an index
            index = int(binary, 2)
            #print(f'index: {index}')

            # check the algorithm for the proper character
            pixel = algorithm[index]
            #print(f'pixel: {pixel}')

            new_image[f'{x_pos},{y_pos}'] = pixel

    return new_image

def print_image(image):
    # figure out how big final input is
    left_x = 0
    right_x = 0
    top_y = 0
    bottom_y = 0
    
    for key in image.keys():
        x,y = list(map(int, key.split(',')))
        if x < left_x:
            left_x = x
        if x > right_x:
            right_x = x
        if y > top_y:
            top_y = y
        if y < bottom_y:
            bottom_y = y

    # find shift values to make this work in a 0-indexed grid
    x_shift = 0 - left_x
    y_shift = 0 - bottom_y

    right_x += x_shift
    top_y += y_shift

    # make the final grid
    grid = []

    for y in range(top_y + 1):
        row = ['.'] * (right_x + 1)
        grid.append(row)

    for key, value in image.items():
        x,y = list(map(int, key.split(',')))
        # grid[int(y)][int(x)] = '#'
        grid[int(y)+y_shift][int(x)+x_shift] = value

    for row in grid:
        print(''.join(row))

    print('')

for i in range(50):
    enhanced_image = enhance(images[-1], enhancement_algorithm, i)
    images.append(enhanced_image)
    #print_image(images[i+1])

pixel_count = 0
for value in images[-1].values():
    if value == '#':
        pixel_count += 1

print_image(images[-1])
print(pixel_count)
