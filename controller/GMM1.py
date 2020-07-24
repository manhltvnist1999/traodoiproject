
import numpy as np
import scipy.io.wavfile as wav
#from sklearn.mixture import gaussian_mixture
from sklearn.mixture import GaussianMixture
import pickle
import warnings
import os
import mfeatures

warnings.filterwarnings("ignore")


def traine(x):
    # file_paths=open("controller/roll_path.txt", 'w')
    # i=1
    # while i<6:
    #     file_paths.write(x+str(i)+".wav\n")
    #     i+=1
    # file_paths.close()
    #
    # #path to training data
    # source   = "training_data/"
    # #path where training speakers will be saved
    # dest = "models/"
    # train_file = "controller/roll_path.txt"
    # file_paths = open(train_file,'r')
    source = "training_data/"
    dest = "models/"
    file_paths = []
    for root, dirs, files in os.walk(os.getcwd() + "\\training_data"):
        for filename in files:
            if (filename.startswith(x)):
                file_paths.append(filename)
    
    count = 1
    # Extracting features for each speaker (5 files per speakers)
    features = np.asarray(())
    for path in file_paths:    
        path = path.strip()
        # read the audio
        rate,sig = wav.read(source+path)

        mfcc_feat= mfeatures.extract_features(sig, rate)
        # extract MFCC 
        
        if features.size == 0:
            features = mfcc_feat
        else:
            features = np.vstack((features, mfcc_feat))
        # when features of 5 files of speaker are concatenated, then do model training
        if count == len(file_paths):
            gmm = GaussianMixture(n_components = 16, max_iter = 200, covariance_type='diag',n_init = 10)
            gmm.fit(features)
            
            # dumping the trained gaussian model
            # picklefile = path.split("-")[0]+".gmm"
            pickle.dump(gmm,open(dest + x + ".gmm",'wb'))
            features = np.asarray(())
            count = 0
        count = count + 1

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
