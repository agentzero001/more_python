import cv2
a = 0
cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:  
    ret, frame = cap.read()
    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    cv2.imshow('Camera', gray_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('p'):
        a+=1
        cv2.imwrite('captured_image{}.jpg'.format(a), frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()