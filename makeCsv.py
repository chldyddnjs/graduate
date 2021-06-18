import pandas as pd
import os
catagories = ["HeadX","HeadY", "NeckX","NeckY", "RShoulderX","RShoulderY", "RElbowX","RElbowY", "RWristX","RWristY",
                "LShoulderX","LShoulderY", "LElbowX","LElbowY", "LWristX","LWristY", "RHipX","RHipY", "RKneeX","RKneeY",
                "RAnkleX","RAnkleY", "LHipX","LHipY", "LKneeX","LKneeY", "LAnkleX","LAnkleY", "ChestX","ChestY","classID"]

df = pd.DataFrame(columns=[catagories])

if not os.path.exists('pos.csv'):
    df.to_csv('pos.csv', index=False, mode='w', encoding='utf-8-sig')
    print('Success')
else:
    df.to_csv('pos.csv', index=False, mode='a', encoding='utf-8-sig', header=False)
    print('Success')