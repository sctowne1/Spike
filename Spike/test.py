def binary_to_string(binary_list):
    binary_string = ""
    for item in binary_list:
        binary_string += str(item)
    return binary_string

def char_to_binary(char):
    decim = ord(char)
    #print(decim)
    binary_char = '{0:08b}'.format(decim)
    return list(binary_char)



def lets_and():
    x = 253 # 11111101
    y = 8 #   00001000
    print(x & y)



lets_and()