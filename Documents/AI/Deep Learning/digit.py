import urllib
import gzip
import numpy as np
import os 
import matplotlib 
#Downloading the database of images from the MNIST webstite
def load_dataset():
    def download(filename, source='http://yann.lecun.com/exdb/mnist/'):
        print("Downloading", filename)
        urllib.urlretrieve(source+filename,filename)
    #Checks if file exists, if not downloads it 
    def load_images(filename):
        if not os.path.exists(filename):
            download(filename)
        #Opens the image and represents it in a 4D Array
        with gzip.open(filename, 'rb') as f:
            data = np.frombuffer(f.read(),np.uint8,offset=16)
            data=data.reshape(-1,1,28,28)
            return data/np.float32(256)
    #Checks if file exists, if not downloads it 
    def load_labels(filename):
        if not os.path.exists(filename):
            download(filename)
        with gzip.open(filename,'rb') as f:
            data = np.frombuffer(f.read(),np.uint8,offset=8)
        return data

    X_train = load_images('train-images-idx3-ubyte.gz')
    y_train = load_labels('train-labels-idx1-ubyte.gz')
    X_test = load_images('t10k-images-idx3-ubyte.gz')
    y_test = load_labels('t10k-labels-idx1-ubyte.gz')
    
    return X_train, y_train, X_test, y_test

X_train, y_train, X_test, y_test = load_dataset()

#shows an immage from the set
matplotlib.use('TkAgg') 

import matplotlib.pyplot as plt 
plt.show(plt.imshow(X_train[3][0]))