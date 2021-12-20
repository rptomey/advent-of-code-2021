with open('aoc21_16_sample2.txt') as f:
    raw_hex_code = f.read()

def hex_to_binary(string):
    binary = ''
    for c in string:
        match c:
            case '0':
                binary_chunk = '0000'
            case '1':
                binary_chunk = '0001'
            case '2':
                binary_chunk = '0010'
            case '3':
                binary_chunk = '0011'
            case '4':
                binary_chunk = '0100'
            case '5':
                binary_chunk = '0101'
            case '6':
                binary_chunk = '0110'
            case '7':
                binary_chunk = '0111'
            case '8':
                binary_chunk = '1000'
            case '9':
                binary_chunk = '1001'
            case 'A':
                binary_chunk = '1010'
            case 'B':
                binary_chunk = '1011'
            case 'C':
                binary_chunk = '1100'
            case 'D':
                binary_chunk = '1101'
            case 'E':
                binary_chunk = '1110'
            case 'F':
                binary_chunk = '1111'
        binary = binary + binary_chunk 
    return binary

def get_characters(source_list, number):
    characters = ''
    for i in range(number):
        characters = characters + source_list.pop(0)
    return characters

def read_literal_packet(source_list):
    binary_value = ''
    while source_list[0] == '1':
        chunk = get_characters(source_list, 5)
        binary_value = binary_value + chunk[1:]
    chunk = get_characters(source_list, 5)
    binary_value = binary_value + chunk[1:]
    return int(binary_value, 2)

def process_packet(source_list):
    version = int(get_characters(source_list, 3), 2)
    print(f'version: {version}')

    type_id = int(get_characters(source_list, 3),2)
    print(f'type: {type_id}')

    if type_id == 4:
        return read_literal_packet(source_list)

    if type_id == 6:
        total_length = int(get_characters(source_list, 15),2)
        print(f'total length: {total_length}')

        sub_list = get_characters(source_list, total_length)






raw_binary = list(hex_to_binary(raw_hex_code))

decoded_packets = []

while raw_binary:
    version = int(get_characters(raw_binary, 3), 2)
    print(f'version: {version}')

    type_id = int(get_characters(raw_binary, 3),2)
    print(f'type: {type_id}')

    if type_id == 4:
        decimal_value = read_literal_packet(raw_binary)

    if type_id == 6:
        length_type_id = get_characters(raw_binary, 1)
        print(f'length type: {length_type_id}')
        
        if length_type_id == '0':
            total_length = int(get_characters(raw_binary, 15),2)
            print(f'total length: {total_length}')
            packets = list(get_characters(raw_binary, total_length))
            binary_value = ''
            print(f'binary value: {binary_value}')
            while packets[0] == '1':
                chunk = get_characters(packets, 5)
                print(f'chunk: {chunk}')
                binary_value = binary_value + chunk[1:]
                print(f'binary value: {binary_value}')
            chunk = get_characters(packets, 5)
            print(f'chunk: {chunk}')
            binary_value = binary_value + chunk[1:]
            print(f'binary value: {binary_value}')

            decimal_value = int(binary_value, 2)

        elif length_type_id == '1':
            sub_packet_number = int(get_characters(raw_binary, 11),2)


    if len(raw_binary) < 6:
        break

print(decimal_value)