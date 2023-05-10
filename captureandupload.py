from os import access
import cv2
from cv2 import VideoCapture
import dropbox
import time
import random
start_time=time.time()
def take_Snapshot():
    number=random.randint(0, 1000)
    VideoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=VideoCaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
        return img_name
def upload__file(img_name):
    access_token="sl.BJsDStcwjWjdhwRbFjiVPfSlLxRimRzYMG8KTfg5hLU-5H4zFCfrSJAnomCWqOa9mmE2pqPQIhz6AdbU2ATzdtjx-Wkpv8xXjin7e7TnVC41L5BflxCL70Iuf6BdAc42chht0sBvcpD5"
    file=img_name
    file_from=file
    file_to="/t/"+(img_name)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")
def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_Snapshot()
            upload__file(name)
main()
