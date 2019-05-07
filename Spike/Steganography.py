##

# Authors: Scott Towne and Jeriah Caplinger

# Description: This file contains the functions used to implement steganography

##

from FileFunctions import select_encoded_file, select_text_file
from PIL import Image
import subprocess
import sys
import numpy as np
import os


#TEXT LSB
# encodes an image with text data using lsb algorithm
def lsb_alg_text(copyLocation):
    file_location = str(select_text_file())
    array = file_location.split("\'")
    file = array[1]
    file_location = file
    
    
    # we open our cover image
    # and get the dimensions of the cover image for use in determining how many
    cover_image = Image.open(copyLocation)
    # pixels there are
    cover_width, cover_height = cover_image.size
    
    # loads our pixels from our cover image
    cover_pixs = cover_image.load()
    encode_a_0 = 254
    encode_a_1 = 1
    
    cover_i= 0
    cover_j = 0
    max_lsb_used = 0
    
    text = open(file_location, "r")
    message_list = list(text.read())
    text.close()
    
    
    # we use these numbers to determine if we can encode the text file into the
    # image
    max_size = (cover_width * cover_height)
    total_bits = len(message_list)


    print("max_size >> " + str(max_size))
    print("total_bits >> " + str(total_bits))
    
    #if we cannot encode the text file
    if total_bits > max_size:
        print("Sorry, the cover image is not big enough to encode the text file.")
        return 0
    
    
    for character in message_list:
        binary_list = char_to_binary(character)
        #we encode every bit in that pixel
        while len(binary_list) != 0:
            bit_to_encode = int(binary_list.pop(0))
            
            # just means we need to go on to the next line
            if cover_j == cover_width:
                cover_j = 0
                cover_i += 1
                # means we are at the end of our image
                if cover_i == cover_height:
                    encode_a_0 = encode_a_0 & 127 # from 11111110 becomes 011111110
                    encode_a_0 = encode_a_0 << 1 # then 11111100
                    encode_a_0 = encode_a_0 | encode_a_1 # finally 11111101
                    # for encoding a 1, it is quite simple: 00000001 becomes 00000010
                    encode_a_1 = encode_a_1 << 1
                    cover_i = 0
                    max_lsb_used += 1
                
                
            get_cover_px = cover_pixs[cover_j, cover_i]
            
            #the section of bits that we are going to encode                 
            get_blue_bits = get_cover_px[2]                
            
            
            if bit_to_encode == 0:
                # we and with because we need to "implant" a 0 in the lsb
                get_blue_bits = get_blue_bits & encode_a_0
                encoded_pixel = (get_cover_px[0], get_cover_px[1], get_blue_bits)
                cover_pixs[cover_j, cover_i] = encoded_pixel
                cover_j += 1
            elif bit_to_encode == 1:
                # we or because we need to "implant" a 1 in the lsb
                get_blue_bits = get_blue_bits | encode_a_1
                encoded_pixel = (get_cover_px[0], get_cover_px[1], get_blue_bits)
                cover_pixs[cover_j, cover_i] = encoded_pixel
                cover_j += 1
        
    cover_image.save(copyLocation)
    
    write_text_key(cover_j, cover_i, max_lsb_used)
    
    print("successfully encoded")    



# decodes lsb algorithm for secret text
def decode_lsb_text(copyLocation):
    # gets all parameters that we need to decode
    key_file = select_text_file()
    key_array = read_key(key_file)
    last_j = int(key_array[0])
    last_i = int(key_array[1])
    max_lsb_used = int(key_array[2])
    
    #gets all the pixels from the encoded image
    encoded_image = Image.open(copyLocation)
    encoded_px = encoded_image.load()
    cover_width, cover_height = encoded_image.size
    
    encode_i = 0
    encode_j = 0
    extract_a_bit = 1
    shift_bits = 0
    # holds the chars and text that make up the secret text
    complete_text = []
    complete_char = []
    
    
    # we iterate through the cover image    
    while encode_i < cover_height and max_lsb_used > 0:
        if encode_i == last_i:
            cover_width = last_j
        while encode_j < cover_width:
            # grab a pixel from the cover image and get the blue bits i.e. the one with the secret data
            encoded_rgb = encoded_px[encode_j, encode_i]
            blue_coded_bits = encoded_rgb[2]
            # we get the lsb
            decoded = blue_coded_bits & extract_a_bit
            decoded = decoded >> shift_bits

            
            complete_char.insert(0, decoded)
            # we continue to do this until we have enough bits to make up a char
            if len(complete_char) == 8:
                # we have to reverse the bit list because of the order of popping/inserting
                complete_char.reverse()
                
                our_char = chr(int(binary_to_string(complete_char), 2))
                # empty our char list
                complete_char = []
                
                complete_text.append(our_char)
            encode_j += 1
        encode_j = 0
        encode_i += 1
        if encode_i == cover_height:
            encode_i = 0
            max_lsb_used = max_lsb_used - 1
            extract_a_bit = extract_a_bit << 1
            shift_bits += 1
    
    
    
    
    # we iterate through the cover image
    while encode_i <= last_i:
        if encode_i == last_i:
            cover_width = last_j
        while encode_j < cover_width:
            # grab a pixel from the cover image and get the blue bits i.e. the one with the secret data
            encoded_rgb = encoded_px[encode_j, encode_i]
            blue_coded_bits = encoded_rgb[2]
            # we get the lsb
            decoded = blue_coded_bits & extract_a_bit
            decoded = decoded >> shift_bits

            
            complete_char.insert(0, decoded)
            # we continue to do this until we have enough bits to make up a char
            if len(complete_char) == 8:
                # we have to reverse the bit list because of the order of popping/inserting
                complete_char.reverse()
                
                our_char = chr(int(binary_to_string(complete_char), 2))
                # empty our char list
                complete_char = []
                
                complete_text.append(our_char)
            encode_j += 1
        encode_j = 0
        encode_i += 1
    
    
    
    if os.path.exists("decoded_message.txt"):
        append_write = 'a' # append if already exists
    else:
        append_write = 'w' # make a new file if not
    
    secrets = open("decoded_message.txt", append_write)
    secrets.write(binary_to_string(complete_text))
    secrets.close()
    
    
    print("successfully decoded")


    
    
# IMAGE LSB
def lsb_alg_img(copyLocation):

    
    # gets our image we want to encode
    secret = copyLocation
    
    
    # we open our secret image
    secret_image = Image.open(secret)
    # pixels there are
    secret_width, secret_height = secret_image.size
    
    secret_size = (secret_width * secret_height)*3
    
    # WE WANT TO ITERATE THROUGH THE ENTIRE LENGTH WISE OF THE PICTURE THEN MOVE
    # TO THE SECOND LINE... so when we do the double loop, we want to do HEIGHT then WIDTH!
    
    
    cover = str(select_encoded_file())
    array = cover.split("\'")
    file = array[1]
    cover = file
    
    
    # we open our cover image
    cover_image = Image.open(cover)
    # we get the dimensions of the secret image for use in determining how many
    # pixels there are
    cover_width, cover_height = cover_image.size
    max_size = cover_width * cover_height
    
    #TODO: this is the check to ensure you can encode the image into the cover
    #TODO: handle this however you want
    if secret_size > max_size:
        print("Sorry, cover image is not big enough to encode in") 
        return 0 
    
    
    # loads our pixels from our cover image
    cover_pixs = cover_image.load()
    #loads our pixels from our secret image
    secret_pixs = secret_image.load()
    
    encode_a_0 = 254
    encode_a_1 = 1
    
    cover_i= 0
    cover_j = 0
    max_lsb_used = 0
    
    i = 0
    j = 0
#    we iterate through each pixel in the image we want to hide
    while i < secret_height:
        while j < secret_width:
            # get the bits that represent that pixel
            secret_bits = pixel_to_binary_list(secret_pixs[j,i])
            #we encode every bit in that pixel
            while len(secret_bits) != 0:
                bit_to_encode = int(secret_bits.pop(0))
                
                # just means we need to go on to the next line
                if cover_j == cover_width:
                    cover_j = 0
                    cover_i += 1
                    # means we are at the end of our image
                    if cover_i == cover_height:
                        encode_a_0 = encode_a_0 & 127 # from 11111110 becomes 011111110
                        encode_a_0 = encode_a_0 << 1 # then 11111100
                        encode_a_0 = encode_a_0 | encode_a_1 # finally 11111101
                        # for encoding a 1, it is quite simple: 00000001 becomes 00000010
                        encode_a_1 = encode_a_1 << 1
                        cover_i = 0
                        max_lsb_used += 1
                    
                    
                get_cover_px = cover_pixs[cover_j, cover_i]
                
                #the section of bits that we are going to encode                 
                get_blue_bits = get_cover_px[2]                
                
                
                if bit_to_encode == 0:
                    # we and with 254 because we need to "implant" a 0 in the lsb
                    get_blue_bits = get_blue_bits & encode_a_0
                    encoded_pixel = (get_cover_px[0], get_cover_px[1], get_blue_bits)
                    cover_pixs[cover_j, cover_i] = encoded_pixel
                    cover_j += 1
                elif bit_to_encode == 1:
                    get_blue_bits = get_blue_bits | encode_a_1
                    encoded_pixel = (get_cover_px[0], get_cover_px[1], get_blue_bits)
                    cover_pixs[cover_j, cover_i] = encoded_pixel
                    cover_j += 1                    
            j += 1
        j = 0
        i  += 1
        
    cover_image.save(copyLocation)
    
    # writes the info we need to decode the image to a text file
    write_key(cover_j, cover_i, secret_width, max_lsb_used)



def decode_lsb_img(copyLocation):
    # we get all parameters that we need to decode the encoded image
    key_file = select_text_file()
    key_array = read_key(key_file)
    last_j = int(key_array[0])
    last_i = int(key_array[1])
    secret_width = int(key_array[2])
    max_lsb_used = int(key_array[3])
    
    
    encoded_image = Image.open(copyLocation)
    cover_width, cover_height = encoded_image.size
    encoded_px = encoded_image.load()
    encode_i = 0
    encode_j = 0
    extract_a_bit = 1
    shift_bits = 0
    # holds bit values for a pixel
    complete_pixel = []
    # holds pixels that make up a line in a picture
    complete_line = []
    # holds the pixels and lines that make up the secret image
    complete_image = []
    
    # we iterate through the cover image
    while encode_i < cover_height and max_lsb_used > 0:
        while encode_j < cover_width:
            # grab a pixel from the cover image and get the blue bits i.e. the one with the secret data
            encoded_rgb = encoded_px[encode_j, encode_i]
            blue_coded_bits = encoded_rgb[2]
            # we get the lsb
            decoded = blue_coded_bits & extract_a_bit
            decoded = decoded >> shift_bits
            
            complete_pixel.insert(0, decoded)
            
            # we continue to do this until we have enough bits to make up a pixel
            if len(complete_pixel) == 24:
                # we have to reverse the bit list because of the order of popping/inserting
                complete_pixel.reverse()
                #RGB bits                
                red_bits = binary_to_string(complete_pixel[0:8])
                green_bits = binary_to_string(complete_pixel[8:16])
                blue_bits = binary_to_string(complete_pixel[16:])

                #RGB bits converted to decimal
                red_value = int(red_bits, 2)
                green_value = int(green_bits, 2)
                blue_value = int(blue_bits, 2)
                
                # finally RGB transferred into pixel format
                decoded_pixel = (red_value, green_value, blue_value)
                # empty our pixel list
                complete_pixel = []
                
                complete_line.append(decoded_pixel)
                # when we have enough pixels to make up a line, we add it to the image
                if len(complete_line)== secret_width:
                    complete_image.append(complete_line)
                    complete_line = []
            encode_j += 1
        encode_j = 0
        encode_i += 1
        if encode_i == cover_height:
            encode_i = 0
            max_lsb_used = max_lsb_used - 1
            extract_a_bit = extract_a_bit << 1
            shift_bits += 1
            

    
    # we iterate through the cover image
    while encode_i <= last_i:
        if encode_i == last_i:
            cover_width = last_j
        while encode_j < cover_width:
            # grab a pixel from the cover image and get the blue bits i.e. the one with the secret data
            encoded_rgb = encoded_px[encode_j, encode_i]
            blue_coded_bits = encoded_rgb[2]
            # we get the lsb
            decoded = blue_coded_bits & extract_a_bit
            decoded = decoded >> shift_bits
            
            complete_pixel.insert(0, decoded)
            
            # we continue to do this until we have enough bits to make up a pixel
            if len(complete_pixel) == 24:
                # we have to reverse the bit list because of the order of popping/inserting
                complete_pixel.reverse()
                #RGB bits                
                red_bits = binary_to_string(complete_pixel[0:8])
                green_bits = binary_to_string(complete_pixel[8:16])
                blue_bits = binary_to_string(complete_pixel[16:])

                #RGB bits converted to decimal
                red_value = int(red_bits, 2)
                green_value = int(green_bits, 2)
                blue_value = int(blue_bits, 2)
                
                # finally RGB transferred into pixel format
                decoded_pixel = (red_value, green_value, blue_value)
                # empty our pixel list
                complete_pixel = []
                
                complete_line.append(decoded_pixel)
                # when we have enough pixels to make up a line, we add it to the image
                if len(complete_line)== secret_width:
                    complete_image.append(complete_line)
                    complete_line = []
            encode_j += 1
        encode_j = 0
        encode_i += 1
        
    # converts our array of pixels to an image that we can display
    array = np.array(complete_image, dtype = np.uint8)
    decoded_image = Image.fromarray(array)
    decoded_image.save(copyLocation)
    
    #spike.display_image()



def binary_to_string(binary_list):
    binary_string = ""
    for item in binary_list:
        binary_string += str(item)
    return binary_string


def write_text_key(cover_j, cover_i, max_lsb_used):
    key_text = str(cover_j) + ", " + str(cover_i) + ", " + str(max_lsb_used)
    key = open("key.txt", "w")
    key.write(key_text)
    
    key.close()
    pid = subprocess.Popen([sys.executable, "KeyWindow.py"])


def write_key(cover_j, cover_i, secret_width, max_lsb_used):
    key_text = str(cover_j) + ", " + str(cover_i) + ", " + str(secret_width) + ", "  + str(max_lsb_used)
    key = open("key.txt", "w")
    key.write(key_text)
    
    key.close()
    pid = subprocess.Popen([sys.executable, "KeyWindow.py"])

def read_key(key):
    key = open(str(key[0]), "r")
    key_string = key.read()
    key_array = key_string.split(", ")
    key.close()
    return key_array


def getActualNum(bitlist):
    out = 0
    for bit in bitlist:
        out = (out << 1) | bit
    return out
    
    



    
# finds the pixel coordinates of the next secret_image pixel to use
def find_coordinates(height, width, height_size, width_size):
    go = True
    # means we are on the last pixel
    if width == width_size - 1 and height == height_size - 1:
        # since we are on the last pixel we set our go boolean to false
        # so the loops will stop accordingly
        go = False
    # means we are on the last pixel for this width and we need to reset    
    elif height == height_size - 1:
        height = 0
        width += 1
    # otherwise, we are free to move to the next pixel to the right    
    else:
        height += 1
    
    return width, height, go
    


def char_to_binary(char):
    decim = ord(char)
    binary_char = '{0:08b}'.format(decim)
    return list(binary_char)

# transforms a pixel to a binary string
def pixel_to_binary_list_print(pixel):
    # the '{}' means store the result as a string with 0 in 0:xxx as the starting
    # position. and x:08 meaning pad with 0's to the left out to the 8th digit
    # the x:xxxb means store it as a binary and format(x) formats the number
    # appropriately after we sum up the tuple
    red_px = '{0:08b}'.format(pixel[0])
    green_px = '{0:08b}'.format(pixel[1])
    blue_px = '{0:08b}'.format(pixel[2])
    print("["+red_px + green_px + blue_px + "]")
    
# transforms a pixel to a binary string
def pixel_to_binary_list(pixel):
    # the '{}' means store the result as a string with 0 in 0:xxx as the starting
    # position. and x:08 meaning pad with 0's to the left out to the 8th digit
    # the x:xxxb means store it as a binary and format(x) formats the number
    # appropriately after we sum up the tuple
    red_px = '{0:08b}'.format(pixel[0])
    green_px = '{0:08b}'.format(pixel[1])
    blue_px = '{0:08b}'.format(pixel[2])
    
    
    
    return list(red_px + green_px + blue_px)
    
