with open('aoc21_16_input.txt') as f:
    raw_hex_code = f.read()

def hex_to_bin(hex: str) -> str:
    return "".join([format(int(h, 16), "b").zfill(4) for h in hex])

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
    global version_sum
    version = int(get_characters(source_list, 3), 2)
    print(f'version: {version}')
    version_sum += version

    type_id = int(get_characters(source_list, 3),2)
    print(f'type: {type_id}')

    if type_id == 4:
        return read_literal_packet(source_list)

    if type_id != 4:
        length_type_id = get_characters(source_list, 1)
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
            sub_packet_number = int(get_characters(source_list, 11),2)
            print(f'sub packets: {sub_packet_number}')

            packets = []
            
            for i in range(sub_packet_number):
                packet = process_packet(source_list)
                print(f'packet: {packet}')
                packets.append(packet)

            print(f'packets: {packets}')
            return packets

raw_binary = list(hex_to_bin(raw_hex_code))

version_sum = 0

decoded_packets = process_packet(raw_binary)

print(decoded_packets)
print(version_sum)