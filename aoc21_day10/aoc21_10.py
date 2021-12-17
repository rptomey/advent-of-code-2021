import re
import statistics

raw_input = []
incomplete_rows = []
corrupted_rows = []
corrupted_score = 0
autocomplete_scores = []

def check_row(string):
    pairings = ['()', '{}', '[]', '<>']
    while any(x in string for x in pairings):
        for pair in pairings:
            string = string.replace(pair, '')
    return string

# with open('aoc21_10_sample.txt') as f:
with open('aoc21_10_input.txt') as f:
    for line in f:
        raw_input.append(line.strip())

for row in raw_input:
    processed = check_row(row)
    if len(processed) > 0 and re.search('[\)\}\>\]]', processed) is None:
        incomplete_rows.append(processed)
    elif len(processed) > 0:
        corrupted_rows.append(processed)

for row in corrupted_rows:
    first_corrupt = re.search('[\)\}\>\]]', row)[0]
    match first_corrupt:
        case ')':
            corrupted_score += 3
        case ']':
            corrupted_score += 57
        case '}':
            corrupted_score += 1197
        case '>':
            corrupted_score += 25137

print(f'Corrupted score: {corrupted_score}')

for row in incomplete_rows:
    row_score = 0
    for character in reversed(row):
        match character:
            case '(':
                row_score *= 5
                row_score += 1
            case '[':
                row_score *= 5
                row_score += 2
            case '{':
                row_score *= 5
                row_score += 3
            case '<':
                row_score *= 5
                row_score += 4
    autocomplete_scores.append(row_score)

print(f'Autocomplete score: {statistics.median(autocomplete_scores)}')