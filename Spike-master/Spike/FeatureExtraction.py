#TODO: High quality images with larger file sizes cause memory leak in currently unknown location. Otherize functions properly.

#TODO: allow user to pass in query image location and directory containing dataset of images to compare to


from SpikeImports import *
import SpikeFunctions
import cv2
import numpy as np
import scipy
import _pickle as pickleRick
import random
import os
import imageio
import matplotlib.pyplot as plt

# Feature extractor
def extract_features(image_path, vector_size=32):
    image = imageio.imread(image_path, pilmode="RGB")
    try:
        # Using KAZE, cause SIFT, ORB and other was moved to additional module
        # which is adding addtional pain during install
        alg = cv2.KAZE_create()
        # Dinding image keypoints
        kps = alg.detect(image)
        # Getting first 32 of them. 
        # Number of keypoints is varies depend on image size and color pallet
        # Sorting them based on keypoint response value(bigger is better)
        kps = sorted(kps, key=lambda x: -x.response)[:vector_size]
        # computing descriptors vector
        kps, dsc = alg.compute(image, kps)
        # Flatten all of them in one big vector - our feature vector
        dsc = dsc.flatten()
        # Making descriptor of same size
        # Descriptor vector size is 64
        needed_size = (vector_size * 64)
        if dsc.size < needed_size:
            # if we have less the 32 descriptors then just adding zeros at the
            # end of our feature vector
            dsc = np.concatenate([dsc, np.zeros(needed_size - dsc.size)])
    except cv2.error as e:
        print('Error: ', e)
        return None
        
    return dsc


def batch_extractor(images_path, pickled_db_path="features.pck"):
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]

    result = {}
    for f in files:
        print('Extracting features from image %s' % f)
        name = f.split('/')[-1].lower()
        result[name] = extract_features(f)
    
    # saving all our feature vectors in pickled file
    with open(pickled_db_path, 'wb') as fp:
        pickleRick.dump(result, fp)
        
class Matcher(object):

    def __init__(self, pickled_db_path="features.pck"):
        with open(pickled_db_path, "rb", buffering=0) as fp:
            self.data = pickleRick.load(fp)
        self.names = []
        self.matrix = []
        for k, v in self.data.items():
            self.names.append(k)
            self.matrix.append(v)
        self.matrix = np.array(self.matrix)
        self.names = np.array(self.names)

    def cos_cdist(self, vector):
        # getting cosine distance between search image and images database
        v = vector.reshape(1, -1)
        np.set_printoptions(threshold=np.nan)
        #print('\n\nVECTOR: ')
        #print(v)
        #print('\n\n')
        #print('\n\nMATRIX: ')
        #print(self.matrix)
        #print('\n\n')
        return scipy.spatial.distance.cdist(self.matrix, v, 'cosine').reshape(-1)

    def match(self, image_path, topn=5):
        features = extract_features(image_path)
        img_distances = self.cos_cdist(features)
        # getting top 5 records
        nearest_ids = np.argsort(img_distances)[:topn].tolist()
        nearest_img_paths = self.names[nearest_ids].tolist()

        return nearest_img_paths, img_distances[nearest_ids].tolist()
        
def show_img(path):

    img = imageio.imread(path, pilmode="RGB")
    plt.imshow(img)
    plt.show()
    
def display(img1, img2):
    #runs SecondaryWindow.py executable
    pid = subprocess.Popen([sys.executable, "SecondaryWindow.py", img1, img2])
    
def parseFilename(file):
        array = file.split("\\")
        filename = array[-1]
        return filename

def run():
    """
    query_img: filepath of img to match
    dataset:   location of directory containing images to compare to
    """
    images_path = 'C:\\Users\\sctow\\Desktop\\Capstone\\Spike-master\\Spike\\Images'
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]
    # getting 3 random images 
    #sample = random.sample(files, 3)
    
    batch_extractor(images_path)

    ma = Matcher('features.pck')
    
    for s in files:
        print('Query image ==========================================')
        #show_img(s)
        names, match = ma.match(s, topn=3)
        print('Result images ========================================')
        best_match = 0
        match_img = ''
        for i in range(3):
            # we got cosine distance, less cosine distance between vectors
            # more they similar, thus we subtract it from 1 to get match value
            print('Match %s' % (1-match[i]))
            if((1-match[i]) > best_match and (1-match[i]) < .98):
                best_match = (1-match[i])
                match_img = i
            
            #show_img(os.path.join(images_path, names[i]))
        display(s,os.path.join(images_path, names[match_img]))
        print("s: ")
        print(parseFilename(s))
        
        print('\nmatch_img: ')
        print(parseFilename(os.path.join(images_path, names[match_img])))

# Uncomment to run file independently for testing
#run()