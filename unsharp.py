import cv2
import sys
import numpy as np
src = cv2.imread(r'C:\Users\user\Desktop\graduate\dataset\Flank\Flank19.jpg')

if src is None:
    print('Image load failed!')
    sys.exit
    
blr = cv2.GaussianBlur(src, (0, 0), 2) # 표준편차 2, 필터 크기는 자동 설정

a = 3.0 # 샤프닝 정도 결정하는 변수
dst = np.clip((1+a)*src - a * blr, 0, 255).astype(np.uint8) # 계산은 정수, 출력은 실수

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imwrite('alter.jpg',dst)
cv2.waitKey()
cv2.destroyAllWindows()