from pprint import pprint as print

all_numbers_raw = [30,35,8,2,39,37,72,7,81,41,25,46,56,18,89,70,0,15,84,75,88,67,42,44,94,71,79,65,58,52,96,83,54,29,14,95,66,61,97,68,57,90,55,32,17,47,20,98,1,69,63,62,31,86,77,85,87,93,26,40,24,19,48,76,73,49,34,45,82,22,80,78,23,6,59,91,64,43,21,51,13,3,53,99,4,28,33,74,12,9,36,50,60,11,27,10,5,16,92,38]
all_numbers = []
for num in all_numbers_raw:
    all_numbers.append(str(num))

called_numbers = []
boards = []

with open('aoc21_4_boards.txt') as f:
    board = []
    row_count = 0
    
    for line in f:
        if str(line.strip()) == "":
            pass
        elif row_count < 4:
            row = line.strip().split()
            board.append(row)
            row_count += 1
        elif row_count == 4:
            row = line.strip().split()
            board.append(row)
            boards.append(board)
            board = []
            row_count = 0

for number in all_numbers:
    called_numbers.append(number)
    print(f'checking number {number}')

    for board in boards:
        print(board)
        # mark called number
        for x in range(5):
            for y in range(5):
                if board[x][y] in called_numbers:
                    board[x][y] = 'x'

        # check the rows
        current_check = 0
        for x in range(5):
            for y in range(5):
                if board[x][y] == 'x':
                    current_check += 1
                else:
                    current_check = 0
                    break
            if current_check == 5:
                print('Winner found.')
                print(board)

                # sum the uncalled numbers for the board
                unchecked_numbers = 0
                for a in range(5):
                    for b in range(5):
                        if board[a][b] != 'x':
                            unchecked_numbers += int(board[a][b])

                print(f'Unchecked values sum: {unchecked_numbers}')
                print(f'Winning number: {number}')
                print(f'Product of values and number {unchecked_numbers * int(number)}')
                quit()

        # check the columns
        current_check = 0
        for y in range(5):
            for x in range(5):
                if board[x][y] == 'x':
                    current_check += 1
                else:
                    current_check = 0
                    break
            if current_check == 5:
                print('Winner found.')
                print(board)

                # sum the uncalled numbers for the board
                unchecked_numbers = 0
                for a in range(5):
                    for b in range(5):
                        if board[a][b] != 'x':
                            unchecked_numbers += int(board[a][b])

                print(f'Unchecked values sum: {unchecked_numbers}')
                print(f'Winning number: {number}')
                print(f'Product of values and number {unchecked_numbers * int(number)}')
                quit()


        

