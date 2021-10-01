import os
from datetime import datetime

path_output = './output.txt'
path_input = './mac.log'
separator = " || "

mac_log_file = None
output_file = None

def get_all_mac_from_output(file_output: str) -> dict: 
    mac_dict = {}
    if(os.path.exists(file_output)):
        with open(file_output, 'r+') as output_file:
            for line in output_file:
                mac_datetime = line.split(separator)
                mac_dict[mac_datetime[0]] = mac_datetime[1][:19]
    else:
        open(file_output, 'w+')

    return mac_dict

def get_new_macs_from_input(file_input: str, dict_with_macs: dict):
    new_macs = {}
    if(os.path.exists(file_input)):
        with open(file_input, 'r') as mac_log_file:
            for line in mac_log_file:
                new_mac = line[:17]

                # if mac not exist in output
                if(not (new_mac in dict_with_macs)):
                    new_macs[new_mac] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    else:
        print('файл', file_input, 'не найден!')

    return new_macs

def write_new_macs_in_output(file_output_path: str, dict_macs: dict, separator: str):
    if(not os.path.exists(file_output_path)):
        open(file_output_path, 'w+')

    with open(file_output_path, 'a') as output_file:
        for key in dict_macs:
            output_file.write(key + separator + dict_macs[key] + '\n')

# example: {'FC AA 14 10 9B 71': '01/10/2021 14:01:24', 'FC 55 14 AA 9B 71': '01/10/2021 14:05:51'}
existing_macs: dict = get_all_mac_from_output(path_output)
print('existing_macs:', existing_macs)

new_macs_dict = get_new_macs_from_input(path_input, existing_macs)

write_new_macs_in_output(path_output, new_macs_dict, separator)