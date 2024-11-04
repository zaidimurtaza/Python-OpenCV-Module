import cv2
import numpy as np
counter=0
circles = np.zeros((4,2),np.int32)
cap = cv2.imread("book.png")
def mouse_pointer_position(event,x,y,flgs,params):
    global counter
    global cap
    if event == cv2.EVENT_LBUTTONDOWN:
        if counter<4:
            circles[counter]= x,y
        counter +=1
       

# cap = cv2.VideoCapture(0)
while True:
    for i in range(0,4):
            cv2.circle(cap,(int(circles[i][0]),int(circles[i][1])),4,(0,0,255),cv2.FILLED)
    if counter == 4:
        width,height = 250,350
        pts1 = np.float32([circles[0],circles[1],circles[2],circles[3]])
        pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
        matrix = cv2.getPerspectiveTransform(pts1,pts2)
        img_output = cv2.warpPerspective(cap,matrix,(width,height))
        
        cv2.imshow("Separated",img_output)
    if cv2.waitKey(1) & 0xFF == ord("q") or counter > 4:
        break

    cv2.imshow("Card",cap)
    cv2.setMouseCallback("Card",mouse_pointer_position)
    cv2.waitKey(1)
