# (c) Copyright 2017 Marc Assens. All Rights Reserved.

__author__ = "Marc Assens"
__version__ = "1.0"



"""
    Utilities with dealing with the dataset
    of 360 Salient Challenge
    API to the 360 salient dataset
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2


def load_image(path):
    """
        Load image into array
        i.e:
        path = "/root/sharedfolder/360Salient/Images/P29.jpg"
    """
    img =  mpimg.imread(path)
    img_size = (img.shape[0], img.shape[1])

    # Resize
    img = cv2.resize(img, (600, 300), interpolation=cv2.INTER_CUBIC)

    # RGB channel first
    # print(img.shape)

    # Remove alpha channel if there is
    if img.shape[2] == 4:
      print('Deleting alpha channel')
      img = img[:,:,:3]

    # Channels first      
    img = img.transpose((2,0,1))

    # Put image into array
    x = np.zeros((1, 3, 300, 600), dtype=np.float32)
    x[0] = img

    return x, img_size

def load_images(path, ids):
    """
        Preprocess and load multiple images into array

        i.e.
            path = '/root/sharedfolder/360Salient/'
            ls 'path' => Images, Scanpaths etc.
    """

    # Output array
    X = np.zeros((len(ids), 3, 300, 600))
    img_sizes = []

    # For each image, get processed image and size
    for i, img_id in enumerate(ids):
        img_path = path + 'Images/P%d.jpg' % img_id
        x , size = load_image(img_path)
        X[i] = x
        img_sizes.append(size)

    return X, img_sizes
def paths_for_images(path, ids):

    paths = []

    # Get the path for each image
    for img_id in ids:
        paths.append(path + 'Images/P%d.jpg' % img_id)

    return paths
    
def get_number_fixations():
    """  
        Get a number of fixaitons for a scanpath. 

        This number is sampled from the distribution
        of number of fixations from the training dataset.
    """

    p = [0.025641025975346565,0.011781011708080769,0.016632016748189926,0.017325017601251602,0.018018018454313278,0.020097021013498306,0.02148302085697651,0.022176021710038185,0.024255024269223213,0.023562023416161537,0.034650035202503204,0.027720028534531593,0.06999307125806808,0.030492030084133148,0.03326403349637985,0.02841302752494812,0.03326403349637985,0.020790020003914833,0.0318780317902565,0.029106028378009796,0.02494802512228489,0.03395703434944153,0.032571032643318176,0.02286902256309986,0.048510048538446426,0.020790020003914833,0.02286902256309986,0.01593901589512825,0.011781011708080769,0.012474012561142445,0.01593901589512825,0.014553014189004898,0.013860014267265797,0.011088010855019093,0.010395010001957417,0.010395010001957417,0.027720028534531593,0.009009009227156639,0.011781011708080769,0.009009009227156639,0.0048510050401091576,0.011088010855019093,0.006237006280571222,0.008316008374094963,0.009702010080218315,0.0048510050401091576,0.006237006280571222,0.006237006280571222,0.008316008374094963,0.0041580041870474815,0.0006930006784386933,0.003465003566816449,0.0013860013568773866,0.0013860013568773866,0.0006930006784386933,0.0,0.0,0.0006930006784386933,0.0,0.0006930006784386933]
    bins = [1.0,2.083333333333333,3.1666666666666665,4.25,5.333333333333333,6.416666666666666,7.5,8.583333333333332,9.666666666666666,10.75,11.833333333333332,12.916666666666666,14.0,15.083333333333332,16.166666666666664,17.25,18.333333333333332,19.416666666666664,20.5,21.583333333333332,22.666666666666664,23.75,24.833333333333332,25.916666666666664,27.0,28.083333333333332,29.166666666666664,30.249999999999996,31.333333333333332,32.416666666666664,33.5,34.58333333333333,35.666666666666664,36.75,37.83333333333333,38.916666666666664,40.0,41.08333333333333,42.166666666666664,43.25,44.33333333333333,45.416666666666664,46.5,47.58333333333333,48.666666666666664,49.75,50.83333333333333,51.916666666666664,53.0,54.08333333333333,55.166666666666664,56.24999999999999,57.33333333333333,58.416666666666664,59.49999999999999,60.58333333333333,61.666666666666664,62.74999999999999,63.83333333333333,64.91666666666666,66.0]
    numb_of_fixations = bins[np.random.choice(60, p=p)]

    return int(numb_of_fixations)