initial_chain = 'VPPHOPVVSFSVFOCOSBKF'
# initial_chain = 'NNCB'

mappings = {}
pairs = {}
characters = {}

# initialize the characters
for char in initial_chain:
    if char in characters:
        characters[char] += 1
    else:
        characters[char] = 1

# read all of the mappings
with open('aoc21_14_input.txt') as f:
# with open('aoc21_14_sample.txt') as f:
    for line in f:
        pair,result = line.strip().split(' -> ')
        if pair not in mappings:
            mappings[pair] = result

# initialize the count of each pair
for i in range(len(initial_chain)-1):
    duo = initial_chain[i] + initial_chain[i+1]
    
    if duo in pairs:
        pairs[duo] += 1
    else:
        pairs[duo] = 1

def polymerize(mappings, pairs, characters):
    iterable_list = list(pairs.items())
    for k,v in iterable_list:
        if v >= 1:
            left = k[0]
            right = k[1]
            insertion = mappings[k]
            
            # the count of the original pair will decrease,
            # but the counts of left+insertion, insertion+right,
            # and the insertion character will all increase by the number of pairs
            modifier = v

            pairs[k] -= v

            new_left = left + insertion
            
            if new_left in pairs:
                pairs[new_left] += modifier
            else:
                pairs[new_left] = modifier
            
            new_right = insertion + right

            if new_right in pairs:
                pairs[new_right] += modifier
            else:
                pairs[new_right] = modifier

            if insertion in characters:
                characters[insertion] += modifier
            else:
                characters[insertion] = modifier

for i in range(40):
    polymerize(mappings, pairs, characters)

max_char = max(characters.keys(), key=(lambda k: characters[k]))
min_char = min(characters.keys(), key=(lambda k: characters[k]))

print(characters[max_char] - characters[min_char])