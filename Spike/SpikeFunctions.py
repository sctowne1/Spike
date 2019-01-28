##

# Authors: Scott Towne and Jeriah Caplinger

# Description: This file contains the functions used to manipulate images in the
#              Spike program

##
from SpikeImports import *



def mirror_image(spike, copyLocation):
    """
    Mirror the image and calls display_image so that the edited version is displayed
    """
    image_obj = Image.open(copyLocation)
    rotated_image = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
    rotated_image.save(copyLocation)
    spike.display_image()

def rotate_image(spike, copyLocation):
    """
    Rotate the given photo 90 degrees and calls display_image
    """
    image = Image.open(copyLocation)
    image = image.transpose(Image.ROTATE_90)
    image.save(copyLocation)
    spike.display_image()
    
def grayscale_image(spike, copyLocation):
    """
    Convert image to grayscale using PIL
    """
    img_obj = Image.open(copyLocation)
    img_obj = img_obj.convert("L") 
    img_obj.save(copyLocation)
    spike.display_image()

def tint_image(spike, copyLocation):
    """
    Used to tint an image with the selected hue.
    """
    #TODO: This method does not work. May not be included in final product. Finishing it will be determined by the amount of time we have left after finishing the core functions of the program.
    
    img_obj = Image.open(copyLocation)
    img_array = np.asarray(img_obj)

    grayscale_image = img_as_float(img_array[::2, ::2])
    image = color.gray2rgb(grayscale_image)
    img_obj = Image.fromarray(image)
    img_obj.save(copyLocation)
    spike.display_image()
    hue_gradient = np.linspace(0, 1)
    hsv = np.ones(shape=(1, len(hue_gradient), 3), dtype=float)
    hsv[:, :, 0] = hue_gradient
    
    all_hues = color.hsv2rgb(hsv)
    
    fig, ax = plt.subplots(figsize=(5, 2))
    # Set image extent so hues go from 0 to 1 and the image is a nice aspect ratio.
    ax.imshow(all_hues, extent=(0, 1, 0, 0.2))
    ax.set_axis_off()
    
    
def invert_image(spike, copyLocation):
    """
    Inverts colors of image using PIL
    """
    image = Image.open(copyLocation)
    inverted_image = PIL.ImageOps.invert(image)
    inverted_image.save(copyLocation)
    spike.display_image()
    
def compare_image(copyLocation, copy_array, copy_count):
    """
    Creates a SecondaryWindow with the most recent and directly previous image using the SecondaryWindow.py file.
    """
    if(copy_count > 1):
        #runs SecondaryWindow.py executable
        pid = subprocess.Popen([sys.executable, "SecondaryWindow.py", copy_array[copy_count%5-2], copyLocation])




def lsb_alg(spike, copyLocation):
    secret_message = "ohhh hello! Silly, I'm a sneaking slippery little snake secret"
    #lsb_alg_text(spike, copyLocation, secret_message)
    #lsb_alg_img(spike, copyLocation)



# encodes an image with text data using lsb algorithm
def lsb_alg_text(spike, copyLocation, message):
    # for getting our cover image to test stuffs for now... we will fix later
    dst_dir = sys.path[0]
    cover = dst_dir + '\\' + 'cover.jpg'
    
    
    # we open our cover image
    # and get the dimensions of the cover image for use in determining how many
    cover_image = Image.open(cover)
    cover_image.save(copyLocation)
    spike.display_image()

    # pixels there are
    cover_width, cover_height = cover_image.size
    
    # loads our pixels from our cover image
    cover_pixs = cover_image.load()
            
    cover_i= 0
    cover_j = 0
    
    message_list = list(message)
    for character in message_list:
        binary_list = char_to_binary(character)
        #we encode every bit in that pixel
        while len(binary_list) != 0:
            bit_to_encode = int(binary_list.pop(0))
            
            # just means we need to go on to the next line
            if cover_j == cover_width:
                cover_j = 0
                cover_i += 1
                
                
            get_cover_px = cover_pixs[cover_j, cover_i]
            
            #the section of bits that we are going to encode                 
            get_blue_bits = get_cover_px[2]                
            
            
            if bit_to_encode == 0:
                # we and with 254 because we need to "implant" a 0 in the lsb
                get_blue_bits = get_blue_bits & 254
                encoded_pixel = (get_cover_px[0], get_cover_px[1], get_blue_bits)
                cover_pixs[cover_j, cover_i] = encoded_pixel
                cover_j += 1
            elif bit_to_encode == 1:
                get_blue_bits = get_blue_bits | 1
                encoded_pixel = (get_cover_px[0], get_cover_px[1], get_blue_bits)
                cover_pixs[cover_j, cover_i] = encoded_pixel
                cover_j += 1
        
    cover_image.save(copyLocation)
    
    spike.display_image()
    
    decode_lsb_text(cover_image, cover_j, cover_i, spike, copyLocation, cover_width)



# decodes lsb algorithm for secret text
def decode_lsb_text(encoded_image, last_j, last_i, spike, copyLocation, cover_width):
    #gets all the pixels from the encoded image
    encoded_px = encoded_image.load()
    encode_i = 0
    encode_j = 0
    extract_a_bit = 1
    # holds the chars and text that make up the secret text
    complete_text = []
    complete_char = []
    
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
    
    # print the string
    print(binary_to_string(complete_text))




def lsb_alg_img(spike, copyLocation):
    # for getting our cover image to test stuffs for now... we will fix later
    dst_dir = sys.path[0]
    cover = dst_dir + '\\' + 'cover.jpg'
    
    
    # we open our cover image
    # and get the dimensions of the cover image for use in determining how many
    cover_image = Image.open(cover)
    # pixels there are
    cover_width, cover_height = cover_image.size
    
    # WE WANT TO ITERATE THROUGH THE ENTIRE LENGTH WISE OF THE PICTURE THEN MOVE
    # TO THE SECOND LINE... so when we do the double loop, we want to do HEIGHT then WIDTH!
    
    #our image we want to hide
    secret = copyLocation
    
    # we open our secret image
    secret_image = Image.open(secret)
    # we get the dimensions of the secret image for use in determining how many
    # pixels there are
    secret_width, secret_height = secret_image.size
    
    # loads our pixels from our cover image
    cover_pixs = cover_image.load()
    #loads our pixels from our secret image
    secret_pixs = secret_image.load()
            
    cover_i= 0
    cover_j = 0
    
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
                    
                    
                get_cover_px = cover_pixs[cover_j, cover_i]
                
                #the section of bits that we are going to encode                 
                get_blue_bits = get_cover_px[2]                
                
                
                if bit_to_encode == 0:
                    # we and with 254 because we need to "implant" a 0 in the lsb
                    get_blue_bits = get_blue_bits & 254
                    encoded_pixel = (get_cover_px[0], get_cover_px[1], get_blue_bits)
                    cover_pixs[cover_j, cover_i] = encoded_pixel
                    cover_j += 1
                elif bit_to_encode == 1:
                    get_blue_bits = get_blue_bits | 1
                    encoded_pixel = (get_cover_px[0], get_cover_px[1], get_blue_bits)
                    cover_pixs[cover_j, cover_i] = encoded_pixel
                    cover_j += 1                    
            j += 1
        j = 0
        i  += 1
        
    cover_image.save(copyLocation)
    
    spike.display_image()
    
    decode_lsb_img(cover_image, cover_j, cover_i, secret_width, spike, copyLocation, cover_width)



def decode_lsb_img(encoded_image, last_j, last_i, secret_width, spike, copyLocation, cover_width):
    #gets all the pixels from the encoded image
    encoded_px = encoded_image.load()
    encode_i = 0
    encode_j = 0
    extract_a_bit = 1
    # holds bit values for a pixel
    complete_pixel = []
    # holds pixels that make up a line in a picture
    complete_line = []
    # holds the pixels and lines that make up the secret image
    complete_image = []
    
    # we iterate through the cover image
    while encode_i < last_i:
        if encode_i == last_i - 1:
            cover_width = last_j
        while encode_j < cover_width:
            # grab a pixel from the cover image and get the blue bits i.e. the one with the secret data
            encoded_rgb = encoded_px[encode_j, encode_i]
            blue_coded_bits = encoded_rgb[2]
            # we get the lsb
            decoded = blue_coded_bits & extract_a_bit
            
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
    spike.display_image()


def binary_to_string(binary_list):
    binary_string = ""
    for item in binary_list:
        binary_string += str(item)
    return binary_string
























def lsb_alg1(spike, copyLocation):
    
    # for getting our cover image to test stuffs for now... we will fix later
    dst_dir = sys.path[0]
    cover = dst_dir + '\\' + 'cover.jpg'
    
    
    # we open our cover image
    # and get the dimensions of the cover image for use in determining how many
    cover_image = Image.open(cover)
    # pixels there are
    cover_width, cover_height = cover_image.size
    
    #cover_size = cover_width * cover_height
    
    #our image we want to hide
    secret = copyLocation
    
    # we open our secret image
    secret_image = Image.open(secret)
    # we get the dimensions of the secret image for use in determining how many
    # pixels there are
    secret_width, secret_height = secret_image.size
    
    #secret_size = secret_width * secret_height
    
    #print("secret size: " + str(secret_size))
    #print('cover size: ' + str(cover_size))
    
    # loads our pixels from our cover image
    cover_pixs = cover_image.load()
    
    
    #loads our pixels from our secret image
    secret_pixs = secret_image.load()
    ##
    print(secret_pixs[0,46])
    print(secret_pixs[0,47])
    print(secret_pixs[0,75])
    print(secret_pixs[0,76])
    print(secret_pixs[0,77])
    print(secret_pixs[0,78])
    print(secret_pixs[0,79])
   # for t in range(225):
    #    specific = secret_pixs[0,t]
     #   print(str(specific[-1]) + ", ")
    ##
    
    
    extract_lsb_from_cover = 1
    
    # width index for the secret image pixel that we are currently on 
    secret_windex = 0
    #height index for the secret image pixel that we are currently on
    secret_hindex = 0
    
    # extracts the pixel at the beginning index and transforms it into a binary
    # list that represents the pixel
    binary_list = []
    count_bits = 24
    
    encode_a_0 = 254
    encode_a_1 = 1
    
    
    ##OPTIONAL FOR TESTING PURPOSES
    counter= 0
    save_j = 0
    max_lsb_used = 0
    secret_bits_counter = 0
    ##


    i = 0
    j = 0
    go = True    
    # iterates through our cover image boolean go tells us when we have reached
    # our last pixel.. len(binary_list) tells us that we still have bits to encode
    while(go or len(binary_list) != 0):
        while(j < cover_height and (go or len(binary_list) != 0)):
            # if we have successfully encoded the entire pixel into the lsb,
            # then we move on to the next pixel
            if (count_bits == 24 and len(binary_list) == 0):
                secret_windex, secret_hindex, go = find_coordinates(secret_hindex, secret_windex, secret_height, secret_width)
                if secret_bits_counter <= 79:
                    print(str(secret_bits_counter) + ": width: " +str(secret_windex) + " height: " + str(secret_hindex))
                binary_list = pixel_to_binary_list(secret_pixs[secret_windex, secret_hindex])
                pixel_to_binary_list_check(secret_pixs[secret_windex, secret_hindex], i, j)
                secret_bits_counter += 1
                
                ## OPTIONAL FOR TESTING PURPOSES
                global total_secret_pixs
                total_secret_pixs += 1
                ##
                
                count_bits = 0
            
            #extract our cover pixel
            extract_pix = cover_pixs[i, j]
            extract_pix_value = extract_pix[-1]
            #NOTE: we encode the bits starting from the LSB!
            bit_to_encode = int(binary_list.pop(0))      
            if i <= 1 and j <= 791 and bit_to_encode == 0:
                print("Ok.... it should be a 1.... i: " + str(i) + " j: " +str(j) )
                print(cover_width)
                print(cover_height)
            if bit_to_encode == 0:
                # this bit wise ands the value with '11111110' so we are
                # able to insert a 0 in the LSB
                extract_pix_value = extract_pix_value & encode_a_0
                
                ##OPTIONAL FOR TESTING PURPOSES
                counter += 1
                ##
                
                # we put our new found value back into the pixel tuple
                encoded_pix = (extract_pix[0], extract_pix[1], extract_pix_value)
                ##
                if i <= 1 and j <= 792:
                    print("Old cover pixel is: " + str(extract_pix) +"    New cover pixel is: " + str(encoded_pix))
                
                ##
                # and put that new encoded pixel into the cover image
                cover_pixs[i,j] = encoded_pix
                count_bits += 1
            # if we are trying to encode a '1' into the LSB    

            elif bit_to_encode == 1:
                #print("encoding 1")
                # this bit wise ors the value with '00000001' so we are able to
                # insert a 1 in the LSB
                extract_pix_value = extract_pix_value | encode_a_1
                
                
                ##OPTIONAL FOR TESTING PURPOSES
                counter += 1
                ##
                
                
                # we put our new found value back into the pixel tuple
                encoded_pix = (extract_pix[0], extract_pix[1], extract_pix_value)
                
                ##
                #if i == 0 and j > 120 and j < 130 :
                #    print("Old cover pixel is: " + str(extract_pix) +"    New cover pixel is: " + str(encoded_pix))
                
                ##
                
                # and put that new encoded pixel into the cover image
                cover_pixs[i,j] = encoded_pix
                
                count_bits += 1
            j += 1
            ##TESTING PURPOSES
        save_j = j
        ##
        j = 0
        i += 1
        # if we finished iterating through our cover image
        if i == cover_width:
            # we have to & with 127 to clear out the greatest 1 bit so when we 
            # left shift, it does not mess us up
            encode_a_0 = encode_a_0 & 127 # from 11111110 becomes 011111110
            encode_a_0 = encode_a_0 << 1 # then 11111100
            encode_a_0 = encode_a_0 | encode_a_1 # finally 11111101
            
            # for encoding a 1, it is quite simple: 00000001 becomes 00000010
            encode_a_1 = encode_a_1 << 1
            #reset back at beginning because we have to do second LSB and so on
            # until we get to the 8th LSB
            i = 0
            max_lsb_used += 1
            
            ##OPTIONAL FOR TESTING PURPOSES
            print("encoding 0 is now: " + str(encode_a_0) + "\nencoding 1 is now: " + str(encode_a_1)   )
            ##
   
    
    ##OPTIONAL FOR TESTING PURPOSES
    print("pixels touched: "+str(counter))
    print("pixels touched in secret image: " + str(total_secret_pixs ))
    print("final i is: " + str(i) +"\nfinal j is: " + str(save_j))
    test_if_different(cover_pixs, cover_width, cover_height)
    ##
    
    
    #displays the cover image with the encoded image inside it
    cover_image.save(copyLocation)
    
    spike.display_image()
    
    decode(cover_image, i, save_j, max_lsb_used, secret_height, copyLocation, spike, secret_pixs)
    


    

    


    
# NOTE: for max_lsb_used, if it is a 1 it means the 1st LSB and part of 2nd LSB was used
def decode1(encoded_image, last_i, last_j, max_lsb_used, secret_height, copyLocation, spike, orig_secret_image):
    #TODO finish and test this decode function 3) implement a text message lsb algorithm
    secret_px_image = []
    secret_px_array = []
    secret_px_list = []
    encoded_width, encoded_height = encoded_image.size
    encoded_pixs = encoded_image.load()
    
    
    ##
    for stuff in range(120, 131):
        print("Encoded pixs: " + str(encoded_pixs[0,stuff]))
    
    ##
    
    
    
    extract_a_bit = 1
    total_times_through = 0
    go = True
    i = 0
    j = 0
    counter = 0
    #does all the iterations of the whole picture
    
    while max_lsb_used > 0:
        while i < encoded_width:
            while j < encoded_height:
                bits = encoded_pixs[i,j]
                specific_bits = bits[-1]
                bit_we_want = specific_bits & extract_a_bit
                # if we have a full pixel that is ready
                if len(secret_px_list) == 24:
                    # we extract the different bits that correspond to RGB
                    ##
                    if i == 0 and j > 120 and j < 131:
                        print("Pixel list is : " +str(secret_px_list))
                        ##
                    red_bits = sum(secret_px_list[0:8])
                    green_bits = sum(secret_px_list[8:16])
                    blue_bits = sum(secret_px_list[16:])
                    # we make a tuple that is ready to be added to the px_array
                    pixel_tuple = (red_bits, green_bits, blue_bits)
                    ##
                    if i == 0 and j > 120 and j < 131:
                        print("Pixel tuple is : " +str(pixel_tuple))
                        ##
                    secret_px_list = []
                    # if we have enough tuple pixels to make a line in the image
                    if len(secret_px_array) == secret_height:
                        # we add it to the image
                        secret_px_image.append(secret_px_array)
                        secret_px_array = []
                    # else we add the tuple to the line array until we have enough    
                    else:
                        secret_px_array.append(pixel_tuple)
                # if we do not have enough bits to make a pixel.. keep adding the bits    
                else:    
                    secret_px_list.insert(0, bit_we_want)
                    
                j += 1
            j = 0
            i += 1
        max_lsb_used = max_lsb_used - 1
        # we want the next LSB in the next iteration
        extract_a_bit = extract_a_bit << 1
        
        
    ##
    stop = True
    which_pix = 0
    dst_dir = sys.path[0]
    cover = dst_dir + '\\' + 'cover.jpg'
    
    
    # we open our cover image
    # and get the dimensions of the cover image for use in determining how many
    cover_image = Image.open(cover)
    # pixels there are
    cover_image_px = cover_image.load()
    ##
    i = 0
    j = 0
    count = 0
    extract_a_bit = 1
    # does the "rest" of the iterations
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    while i < last_i:
        while j < last_j:
            bits = encoded_pixs[i,j]
            specific_bits = bits[-1]
            bit_we_want = specific_bits & extract_a_bit
            
            ##
            #if i == 0:
                #print(str(specific_bits))
                ##
                
            # if we have a full pixel that is ready
            if len(secret_px_list) == 24:
                secret_px_list.reverse()
                print("****************"+ str(which_pix) +"*************************")
                print("EXTRACTED DATA: \n"+ str(secret_px_list))
                print("ORIGINAL SECRET IMAGE:")
                pixel_to_binary_list_print(orig_secret_image[0, which_pix])
                print("\nORIGINAL COVER IMAGE:")
                pixel_to_binary_list_print(cover_image_px[0,which_pix])
                print("COVER IMAGE WITH SECRET DATA:")
                pixel_to_binary_list_print(encoded_pixs[0,which_pix])
                
                print("************************************\n\n")
                
                which_pix += 1
                
                ##
                #if i == 0 and j > 120 and j < 131:
                    #print("Pixel list is : " +str(secret_px_list))
                    ##
                # we extract the different bits that correspond to RGB
                red_bits = getActualNum(secret_px_list[0:8])
                ##
                #if i == 0 and j > 120 and j < 131:
                    #print("red bits : " +str(red_bits))
                    ##
                green_bits = getActualNum(secret_px_list[8:16])
                ##
                #if i == 0 and j > 120 and j < 131:
                    #print("green bits : " +str(green_bits))
                    ##
                blue_bits = getActualNum(secret_px_list[16:])
                ##
                #if i == 0 and j > 120 and j < 131:
                #if count < 225:
                 #   print(str(blue_bits) + ", " )
                  #  count += 1
                    ##
                # we make a tuple that is ready to be added to the px_array
                pixel_tuple = (red_bits, green_bits, blue_bits)
                ##
                #if i == 0 and j > 120 and j < 131:
                    #print("Pixel tuple is : " +str(pixel_tuple))
                    ##
                secret_px_list = []
                # if we have enough tuple pixels to make a line in the image
                if len(secret_px_array) == secret_height:
                    ##
                    #if stop:
                        #print(secret_px_array)
                        #stop = False
                        ##
                    # we add it to the image
                    secret_px_image.append(secret_px_array)
                    secret_px_array = []
                # else we add the tuple to the line array until we have enough    
                else:
                    secret_px_array.append(pixel_tuple)
            # if we do not have enough bits to make a pixel.. keep adding the bits    
            else:    
                secret_px_list.insert(0, bit_we_want)
                if which_pix <= 74 and bit_we_want != 1:
                    print("HOUSTENNNNNN WE GOT A PROBLEM@@@@@@@@@@@@@@@@@@@@@@@\ti: " +str(i)+" j: " +str(j) )
                
            j += 1
        j = 0
        i += 1
        
    ##
    #print(len(secret_px_image[0]))
    #print(secret_px_image[0])
    ##
        
    array = np.array(secret_px_image, dtype = np.uint8)
    decoded_image = Image.fromarray(array)
    decoded_image.save(copyLocation)
    spike.display_image()



def getActualNum(bitlist):
    out = 0
    for bit in bitlist:
        out = (out << 1) | bit
    return out



# SANITY TEST
def test_if_different(encoded_pixs, width, height):
    # for getting our cover image to test stuffs for now... we will fix later
    dst_dir = sys.path[0]
    original = dst_dir + '\\' + 'cover.jpg'
    orig_image = Image.open(original)
    
    original_pixs = orig_image.load()
    
    counter = 0
    
    for i in range(0, width):
        for j in range(0, height):
            encoded_sum = sum(encoded_pixs[i,j])
            original_sum = sum(original_pixs[i,j])
            #result = encoded_sum - original_sum
            if encoded_sum != original_sum:
                counter += 1
            result = encoded_sum - original_sum
    print("total number of different pixels is >> " + str(counter))
    
    



    
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
    
    

# transforms a pixel to a binary string
def pixel_to_binary_list_check(pixel, i, j):
    # the '{}' means store the result as a string with 0 in 0:xxx as the starting
    # position. and x:08 meaning pad with 0's to the left out to the 8th digit
    # the x:xxxb means store it as a binary and format(x) formats the number
    # appropriately after we sum up the tuple

    if i == 1 and j < 792 :
        print("SUMMMMMMMMMMMMMMMMMMMMBITCHHHHHHHHHHHHHHHHHHHHHHHHH: "+ str(pixel))


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
    