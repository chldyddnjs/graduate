import cv2
import numpy as np
import os
import sys

protoFile = r'C:\Users\user\Desktop\graduate\openpose\models\pose\mpi\pose_deploy_linevec_faster_4_stages.prototxt'
weightFile = r'C:\Users\user\Desktop\graduate\openpose\models\pose\mpi\pose_iter_160000.caffemodel'
min_confidence = 0.1

BODY_PARTS = { "Head": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
                "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
                "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "Chest": 14,
                "Background": 15 }

POSE_PAIRS = [ ["Head", "Neck"], ["Neck", "RShoulder"], ["RShoulder", "RElbow"],
                ["RElbow", "RWrist"], ["Neck", "LShoulder"], ["LShoulder", "LElbow"],
                ["LElbow", "LWrist"], ["Neck", "Chest"], ["Chest", "RHip"], ["RHip", "RKnee"],
                ["RKnee", "RAnkle"], ["Chest", "LHip"], ["LHip", "LKnee"], ["LKnee", "LAnkle"] ]

net = cv2.dnn.readNetFromCaffe(protoFile,weightFile)

def detectAndDisplay(img,path):
    if img is None:
        print('Wrong path:')
        sys.exit(0)
    else:
        img = cv2.resize(img, dsize=(368,368))

    img = cv2.resize(img,(368,368),cv2.INTER_LANCZOS4)
    width,height,channels = img.shape

    blob = cv2.dnn.blobFromImage(img,0.00392,(368,368),(0,0,0),swapRB=False,crop = False)

    net.setInput(blob)

    output = net.forward()

    #output[0]는 이미지 ID
    h = output.shape[2]
    w = output.shape[3]
 
    points = []
    data = []
    for i in range(0,15):
        #output.shape[1]은 신체부위에 대한 신뢰도
        confidences = output[0,i,:,:]
        #global 최대값 찾기
        minVal,confidence,minLoc,point = cv2.minMaxLoc(confidences)

        #원래 이미지에 맞게 점위치 변경
        x = int((width * point[0]) / w)
        y = int((height * point[1]) / h)
        # x-= 150
        # y+= 100

        if min_confidence < confidence:
            cv2.circle(img,(x,y),3,(0,255,255),thickness=-1,lineType=cv2.FILLED)
            cv2.putText(img, "{}".format(i), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, lineType=cv2.LINE_AA)
            points.append((x,y))
            data.append(int(x))
            data.append(int(y))
        else:
            points.append(None)
            data.append(0)
            data.append(0)
    # cv2.imshow(path,img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    imageCopy = img

    # 각 POSE_PAIRS별로 선 그어줌 (머리 - 목, 목 - 왼쪽어깨, ...)
    for pair in POSE_PAIRS:
        partA = pair[0]             # Head
        partA = BODY_PARTS[partA]   # 0
        partB = pair[1]             # Neck
        partB = BODY_PARTS[partB]   # 1
        
        #print(partA," 와 ", partB, " 연결\n")
        if points[partA] and points[partB]:
            cv2.line(imageCopy, points[partA], points[partB], (0, 255, 0), 2)


    # cv2.imshow("test",imageCopy)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return data
#데이터셋 만들기
import pandas as pd
os.chdir('dataset')
img_path = 'dataset/'
paths = []
for current_dir,dirs,files in os.walk('.'):
    for file in files:
        new_path = img_path + current_dir[2:] + '/'
        if file.endswith('.jpg'):
            new_path = new_path + file
            paths.append(new_path)

#본인에게 맞는 경로를 사용하세요
os.chdir(r'C:\Users\user\Desktop\graduate')
print(paths)
for path in paths:
    img = cv2.imread(path)
    new_data = detectAndDisplay(img,path)
    if path[8:13] == 'Squat':
        new_data.append(1)
    if path[8:13] == 'Stand':
        new_data.append(0)
    # if 레그레이션 준비자세
    #   new_data.append(2)
    # if 레그레이션 동작자세
    #   new_data.append(3)
    # if 플랭크 준비자세
    #   new_data.append(4)
    # if 플랭크 동작 자세
    #   new_data.append(5)
    df = pd.DataFrame([new_data])

    if len(new_data) == 31:
        if not os.path.exists('pos.csv'):
            df.to_csv('pos.csv', index=False, mode='w', encoding='utf-8-sig')
            print('Success')
        else:
            df.to_csv('pos.csv', index=False, mode='a', encoding='utf-8-sig', header=False)
            print('Success')