import cv2
def takesnapshots():
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        cv2.imwrite("Newpicture1.jpg",frame)
        result=False 

    videoCaptureObject.release()
    cv2.destroyAllWindows()   
takesnapshots()



