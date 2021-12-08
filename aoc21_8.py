easy_counts = [0] * 10
output_sum = 0

with open('aoc21_8_input.txt') as f:
    for line in f:
        components = line.split('|')
        key = components[0].strip().split()
        output = components[1].strip().split()

        # part one
        for item in output:
            length = len(item)
            match length:
                case 2:
                    easy_counts[1] += 1
                case 4:
                    easy_counts[4] += 1
                case 3:
                    easy_counts[7] += 1
                case 7:
                    easy_counts[8] += 1

        # part two
        # establish all of the slots (single characters) and shapes (arrays)
        right_vertical = []
        middle_L = []
        top_horizonal = ''
        middle_horizontal = ''
        bottom_horizontal = ''
        bottom_left_vertical = ''
        top_left_vertical = ''
        bottom_right_vertical = ''
        top_right_vertical = ''

        # find the right side first
        for item in key:
            if len(item) == 2:
                right_vertical = list(item)
                break
        
        # find the 7 to get the top_horizontal
        for item in key:
            if len(item) == 3:
                for c in item:
                    if c not in right_vertical:
                        top_horizonal = c
                        break
                else: # special use of for-else will only go to else if the inner loop finished without breaking
                    continue
                break
        
        # find the 4 to get the middle_L
        for item in key:
            if len(item) == 4:
                for c in item:
                    if c not in right_vertical and c != top_horizonal:
                        middle_L.append(c)
                break

        # use info to find the 9 and the bottom_horizontal
        for item in key:
            if len(item) == 6:
                unmatched = []
                for c in item:
                    if c not in right_vertical and c not in middle_L and c != top_horizonal:
                        unmatched.append(c)
                if len(unmatched) == 1:
                    bottom_horizontal = unmatched[0]
                    break
        
        # using all possible characters and info so far, find bottom_left_vertical
        all_characters = 'abcdefg'
        for c in all_characters:
            if c not in right_vertical and c not in middle_L and c != top_horizonal and c != bottom_horizontal:
                bottom_left_vertical = c
                break

        # three slots positively identified, four to go

        # find the 6 (all known slots plus middle_L) to get bottom_right_vertical
        for item in key:
            print('looking for 6')
            if len(item) == 6: # narrowed down to 6, 9, or 0
                print(item)
                unmatched = []
                for c in item:
                    print(f'testing: {c}')
                    print(f'right vert = {right_vertical}')
                    print(f'midlle L = {middle_L}')
                    print(f'top horiz = {top_horizonal}')
                    print(f'bot horiz = {bottom_horizontal}')
                    print(f'bot lef = {bottom_left_vertical}')
                    if c in right_vertical and c not in middle_L and c != top_horizonal and c != bottom_horizontal and c != bottom_left_vertical:
                        unmatched.append(c)
                print(f'unmatched = {unmatched}')
                print(f'umatch len = {len(unmatched)}')
                print(f'right vert = {right_vertical}')
                print(c in right_vertical)
                if len(unmatched) == 1:
                    print('hello')
                    bottom_right_vertical = unmatched[0]
                    break

        # get top_right_vertical
        for c in right_vertical:
            if c != bottom_right_vertical:
                top_right_vertical = c
                break

        # 6 and 0 are still ambiguous because of middle_L, but we know enough about 2 to find middle_horizontal
        for item in key:
            if len(item) == 5:
                unmatched = []
                for c in item:
                    if c != top_horizonal and c != bottom_horizontal and c != bottom_left_vertical and c != top_right_vertical:
                        unmatched.append(c)
                if len(unmatched) == 1:
                    middle_horizontal = unmatched[0]
                    break
        
        # get top_left_vertical
        for c in middle_L:
            if c != middle_horizontal:
                top_left_vertical = c
                break

        # all slots identified
        print(right_vertical)
        print(top_horizonal)
        print(middle_L)
        print(bottom_horizontal)
        print(bottom_left_vertical)
        print(bottom_right_vertical)
        print(top_right_vertical)
        print(middle_horizontal)
        print(top_left_vertical)

        # now decode the output
        decoded = ''
        for item in output:
            # can still use the easy identifications to save some decoding
            length = len(item)
            match length:
                case 2:
                    decoded += '1'
                case 4:
                    decoded += '4'
                case 3:
                    decoded += '7'
                case 7:
                    decoded += '8'
                case 5: # can only be 2, 3, or 5
                    if bottom_left_vertical in item:
                        decoded += '2'
                    elif top_left_vertical in item:
                        decoded += '5'
                    else:
                        decoded += '3'
                case 6: # can only be 6, 9, or 0
                    if middle_horizontal not in item:
                        decoded += '0'
                    elif bottom_left_vertical not in item:
                        decoded += '9'
                    else:
                        decoded += '6'

        # decode the key to check...
        decoded_key = ''
        for item in key:
            # can still use the easy identifications to save some decoding
            length = len(item)
            match length:
                case 2:
                    decoded_key += '1'
                case 4:
                    decoded_key += '4'
                case 3:
                    decoded_key += '7'
                case 7:
                    decoded_key += '8'
                case 5: # can only be 2, 3, or 5
                    if bottom_left_vertical in item:
                        decoded_key += '2'
                    elif top_left_vertical in item:
                        decoded_key += '5'
                    else:
                        decoded_key += '3'
                case 6: # can only be 6, 9, or 0
                    if middle_horizontal not in item:
                        decoded_key += '0'
                    elif bottom_left_vertical not in item:
                        decoded_key += '9'
                    else:
                        decoded_key += '6'

        print(f'Key: {key}')
        print(f'Decoded key: {decoded_key}')
        print(f'Output: {output}')
        print(f'Decoded: {decoded}')
        output_sum += int(decoded)
        print(f'Running total: {output_sum}')




# part one output
print(f'The easy digits appeared {sum(easy_counts)} times.')

# part two output
print(f'The sum of the fully decoded outputs is {output_sum}')