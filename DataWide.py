import cv2
import os
os.chdir('dataset')
img_path = ''

# 모든 이미지파일 경로 가져오기
for current_dir,dirs,files in os.walk('.'):
    numbering =0
    if current_dir[2:] == 'Squat':
        #가변적이다
        numbering = 80
    if current_dir[2:] == 'Stand':
        #가변적이다
        numbering = 85
    for file in files:
        new_path = img_path + current_dir[2:] +'/'
        dir_path = new_path
        if file.endswith('.jpg'):
            new_path = new_path + file
            img = cv2.imread(new_path)
            if img is None:
                print('fuck')
            else:
                print(new_path)
            imgCopy = cv2.flip(img,1)
            dir_path = dir_path + current_dir[2:] + str(numbering) + '.jpg'
            cv2.imwrite(dir_path,imgCopy)
            numbering=numbering+1
            print(numbering)
           
os.chdir(r'C:\Users\user\Desktop\graduate')