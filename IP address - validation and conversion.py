def is_num(s: str) -> bool:
    return all(digit in "0123456789" for digit in s)

def is_valid_ipv4(address: str) -> bool:
    octets = address.split('.')
    if len(octets) == 4 and all(is_num(octet) for octet in octets):
        if all(0<=int(octect)<256 for octect in octets) and int(octets[0])!=0:
            return True
    return False

def bin_ipv4(address: str) -> str:
    octets = [int(octet) for octet in address.split('.')]
    return '.'.join([bin(octet)[2:].rjust(8,'0') for octet in octets])

def oct_ipv4(address:str) -> str:
    octets = [int(octet) for octet in address.split('.')]
    return '.'.join([oct(octet)[2:] for octet in octets])

def hex_ipv4(address: str) -> str:
    octets = [int(octet) for octet in address.split('.')]
    return '.'.join([hex(octet)[2:] for octet in octets]).upper()

def input_valid(count: int) -> list:
    valid, to_input = list(), count
    while True:
        input_list = list()
        print("\nEnter {} addresses below: ".format(to_input))
        for i in range(to_input):
            input_list.append(input())
        valid += [el for el in input_list if is_valid_ipv4(el)]
        if len(valid) == count:
            return tuple(valid)
        to_input = count - len(valid)
        print("The values",[el for el in input_list if el not in valid],"are invalid")


def line(group: list) -> str:
    return group[0].rjust(18) + group[1].rjust(40) + group[2].rjust(18) + group[3].rjust(18) + "\n"


#main
#input and conversion
print("Enter valid ipv4 addresses, seperated by the enter key")
addresses = input_valid(10)
converted = list()
for address in addresses:
    converted.append([address, bin_ipv4(address), oct_ipv4(address), hex_ipv4(address)])
print("\nThe addresses have been converted\n")

#display and storage
conversion_f = open("conversion.txt",'w')
header =  "Decimal".rjust(18) + "Binary".center(40) + "Octal".rjust(18) + "Hexadecimal".rjust(18) + "\n"
conversion_f.write(header + '\n')
print(header)
index = 0
for group in converted:
    conversion_f.write(line(group))
    print(" " + str(index) + line(group))
    index += 1
conversion_f.close()
print("The addresses have been stored into the file 'conversion.txt'")
input()
