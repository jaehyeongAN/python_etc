import pandas as pd 
import os, time 
from keras.preprocessing.image import load_img, save_img
import cv2
import matplotlib.pyplot as plt

img_list = os.listdir()	# 경로 내 이미지 목록
save_path = os.getcwd()+'/image/' # 저장 할 경로 


''' keras.preprocessing.image '''
start = time.time()
for i in img_list:
	img = load_img(i)
	img_name = i.split('.')[0]
	save_img(save_path+img_name+'_jh.jpg', img)
print(time.time() - start)

''' cv2 '''
# start = time.time()
# for i in img_list:
# 	img = cv2.imread(i)
# 	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# 	img_name = i.split('.')[0]

# 	cv2.imwrite(save_path+img_name+'_jh.jpg', cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# print(time.time() - start)