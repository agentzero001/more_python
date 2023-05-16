import cv2

a = 0
cap = cv2.VideoCapture(0)

while True:  
    ret, frame = cap.read()
    
    cv2.imshow('Camera', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('p'):
        a+=1
        cv2.imwrite('captured_image{}.jpg'.format(a), frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()