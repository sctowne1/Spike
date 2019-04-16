from PIL import Image
import SpikeFunctions

 

"""
img1 = str(SpikeFunctions.select_cover_file())
array = img1.split("\'")
file = array[1]
img1 = file

img2 = str(SpikeFunctions.select_cover_file())
array = img2.split("\'")
file = array[1]
img2 = file

i1 = Image.open(img1)
i2 = Image.open(img2)
assert i1.mode == i2.mode, "Different kinds of images."
assert i1.size == i2.size, "Different sizes."

pairs = zip(i1.getdata(), i2.getdata())
if len(i1.getbands()) == 1:
    # for gray-scale jpegs
    dif = sum(abs(p1-p2) for p1,p2 in pairs)
else:
    dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))

ncomponents = i1.size[0] * i1.size[1] * 3
perc_diff = (dif / 255.0 * 100) / ncomponents

print(perc_diff)
    
"""