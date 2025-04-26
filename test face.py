import cv2

print("OpenCV version:", cv2.__version__)
print("cv2.face exists:", hasattr(cv2, 'face'))

if hasattr(cv2, 'face'):
    clf = cv2.face.LBPHFaceRecognizer_create()
    print("LBPHFaceRecognizer successfully created!")
else:
    print("cv2.face is still missing. Check your installation.")
