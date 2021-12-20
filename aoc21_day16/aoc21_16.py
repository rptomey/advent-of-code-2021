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

    if type_id != 4:
        length_type_id = get_characters(raw_binary, 1)
        print(f'length type: {length_type_id}')

        if length_type_id == '0':
            total_length = int(get_characters(source_list, 15),2)
            print(f'total length: {total_length}')

            sub_list = list(get_characters(source_list, total_length))
            print(f'sub list: {sub_list}')

            packets = []

            while sub_list:
                packet = process_packet(sub_list)
                print(f'packet: {packet}')
                packets.append(packet)

            print(f'packets: {packets}')
            return packets
        
        elif length_type_id == '1':
            sub_packet_number = int(get_characters(raw_binary, 11),2)
            print(f'sub packets: {sub_packet_number}')

            packets = []
            
            for i in range(sub_packet_number):
                packet = process_packet(source_list)
                print(f'packet: {packet}')
                packets.append(packet)

            print(f'packets: {packets}')
            return packets


raw_binary = list(hex_to_binary(raw_hex_code))

decoded_packets = process_packet(raw_binary)

print(decoded_packets)