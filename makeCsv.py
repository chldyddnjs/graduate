from numpy.core.numeric import False_
import pandas as pd

catagories = ["HeadX","HeadY", "NeckX","NeckY", "RShoulderX","RShoulderY", "RElbowX","RElbowY", "RWristX","RWristY",
                "LShoulderX","LShoulderY", "LElbowX","LElbowY", "LWristX","LWristY", "RHipX","RHipY", "RKneeX","RKneeY",
                "RAnkleX","RAnkleY", "LHipX","LHipY", "LKneeX","LKneeY", "LAnkleX","LAnkleY", "ChestX","ChestY"]
input = [168, 8, 176, 56, 144, 64, 120, 96, 136, 56.1, 216, 72, 224, 120.1, 232, 160, 160.1, 152, 168.1, 232.1, 184, 304, 208, 152.1, 184.1, 224.1, 200, 304.1, 184.2, 112]
data = dict()
for i in range(0,30):
    data[catagories[i]] = int(input[i])
df = pd.DataFrame([data],columns=["HeadX","HeadY", "NeckX","NeckY", "RShoulderX","RShoulderY", "RElbowX","RElbowY", "RWristX","RWristY",
                "LShoulderX","LShoulderY", "LElbowX","LElbowY", "LWristX","LWristY", "RHipX","RHipY", "RKneeX","RKneeY",
                "RAnkleX","RAnkleY", "LHipX","LHipY", "LKneeX","LKneeY", "LAnkleX","LAnkleY", "ChestX","ChestY"])
df.to_csv('pos.csv',header=False,index=False)