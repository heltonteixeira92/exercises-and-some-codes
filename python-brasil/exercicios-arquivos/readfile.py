"""
HOW CAN I IDENTIFY A VALID IP ADDRESS?
- Check that the address consists of four decimal numbers separeted by dots.
- Check that each decimal number is between 0 and 255.
- Check that the first decimal number is not 0, it is reserved for special purposes.
- Check that the last decimal number is not 255, as it is reserved for broadcast addresses.
"""

file = 'ip.txt'


def ipv4_validation(ipv4):
    # validation 1
    if not ipv4.count('.') == 3:
        return False

    # validation 2
    decimals = ipv4.split('.')
    for i in decimals:
        if int(i) > 255 or int(i) < 0:
            return False

    # validation 3
    if decimals[0] == 0:
        return False

    # validation 4
    if decimals[-1] == 255:
        return False

    return True


def read_file(filename):
    valid_ip_list = []
    invalid_ip_list = []
    with open(filename, 'r') as arquivo_cpf:
        for linha in arquivo_cpf:
            ip = linha.strip()
            if ipv4_validation(ip):
                valid_ip_list.append(ip)
            else:
                invalid_ip_list.append(ip)

    return valid_ip_list, invalid_ip_list


def nice_print(valid_data, invalid_data):

    valid_data.insert(0, '[Endereços válidos:]')
    invalid_data.insert(0, '[Endereços inválidos:]')

    for valid_p in valid_data:
        print(valid_p)

    print()

    for invalid_p in invalid_data:
        print(invalid_p)


valid, invalid = read_file(file)
print(nice_print(valid, invalid))