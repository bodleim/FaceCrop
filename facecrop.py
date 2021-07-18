import cv2
import os

face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
eye_casecade = cv2.CascadeClassifier('./haarcascade_eye.xml')

count = 1
targetFolder = 'rlawodnjs'

if not os.path.exists('processed'):
    os.mkdir('processed')
if not os.path.exists('processed/' + targetFolder):
    os.mkdir('processed/' + targetFolder)


def crop():
    global count

    img = cv2.imread(r'.\data\\'+targetFolder+'\\'+str(count)+'.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3,5)
    imgNum  = 0

    key = cv2.waitKey(0) & 0xFF # 키보드 입력을 무한 대기, 8비트 마스크처리
    cv2.imshow('ImageProcessing', img)

    try:
        print(str(count) + '번째 이미지 프로세싱중.')
        for (x,y,w,h) in faces:
            cropped = img[y - int(h / 4):y + h + int(h / 4), x - int(w / 4):x + w + int(w / 4)]
            # 이미지를 저장
            cv2.imwrite('./processed/'+targetFolder+'/'+ targetFolder + '_' + str(count) + "["+str(imgNum)+"].jpg", cropped)
            imgNum += 1

            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            eyes = eye_casecade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh),(0,255,0),2)
    except:
        print("[Facecrop] 사진에서 얼굴을 검출하지 못하여 다음사진으로 넘어갑니다.")
        count += 1
        cv2.destroyWindow('ImageProcessing')
        crop()

    count += 1
    cv2.destroyWindow('ImageProcessing')
    crop()

    if key == ord('s'):
        cv2.destroyAllWindows()
        quit()

crop()