# 2. 동영상 처리
# 영상 읽기
# 영상 출력

import cv2 # 패키지 불러오기

cap = cv2.VideoCapture(0) # 웹캠 불러오기
print(cap. isOpened()) # 영상이 열리냐 안 열리냐
while(cap. isOpened()): # 열리면 반복문 실행
    ret, frame = cap.read() # read를 하면 두 가지 값을 반환해줌
    # frame이 불러와지면 true, 아니면 false
    if ret : # 만약 이미지 객체가 생성됐으면
        cv2.imshow('frame', frame) # frame 보여줌

        if cv2.waitKey(1) & 0xFF == ord('q'): # 0.001초씩 보여주면서 q키 누르면 break로 나가는 것
            break
        
    else:
        break

cap.release()
cv2.destroyAllWindows()

# 영상 쓰기

import cv2

cap = cv2.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

print(cap.isOpened())
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        out.write(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()

# 영상에 문자 넣기
# 영상에 시간 넣기

import cv2
import datetime
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#cap.set(3, 1208) #width
#cap.set(4, 720) #height
#print(cap.get(3))
#print(cap.get(4))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret :
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: ' + str(cap.get(3)) + ' ' 