# coding = utf-8
# author: huyz
# Created on Apr 13 23:03:29 2019

import os
import numpy as np
import pandas as pd
from tqdm import tqdm
from scipy import misc

emotions = {'0': 'Anger', '1': 'Disgust', '2': 'Fear', '3': 'Happy', '4': 'Sad', '5': 'Surprised', '6': 'Neutral'}

def creat_foler(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

def save_image(csv_file):
    pd_data = pd.read_csv(open(csv_file))
    
    num_pd_data = len(pd_data)
    for index in tqdm(range(num_pd_data)):
        emotion = pd_data.loc[index][0]
        pixel = pd_data.loc[index][1]
        usage = pd_data.loc[index][2]
        
        pixel_array = np.asarray(list(map(float, pixel.split())))
        image = pixel_array.reshape(48, 48)
        
        emotion_name = emotions[str(emotion)]
        dst_dir = os.path.join('./images', usage, emotion_name)
        creat_foler(dst_dir)
        
        img_path = os.path.join(dst_dir, str(index)+'.jpg')
        
        misc.toimage(image).save(img_path)

if __name__ == '__main__':
    csv_path = 'E:/表情识别/emotion_classifier_tensorflow_version/fer2013/fer2013.csv'
    save_image(csv_path)