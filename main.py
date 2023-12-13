# import streamlit as st
import cv2
import pandas as pd
import subprocess
from datetime import datetime
import time


# Set the initial time
start_time = time.perf_counter()

# Set the delay in seconds
delay = 60


df = pd.DataFrame({"Status":[True, False, False, False, False, False]}) 


cap = cv2.VideoCapture('../easy.mp4')

count=0

ind_location = 0
total_len = len(df) - 1
# git_commit_and_push()

df.to_csv('saved.csv', index= False)

while True:    

    ret, frame = cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    cv2.imshow("IMSHOW", frame)
    elapsed_time = time.perf_counter() - start_time
    if elapsed_time >= delay:
        print(ind_location)

        ind_location += 1
        df["Status"].iloc[ind_location] = True
        df["Status"].iloc[ind_location-1] = False

        df.to_csv('saved.csv', index= False)
        print(df)

        if ind_location == total_len:
            ind_location = -1

        start_time = time.perf_counter()


    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

    

cv2.destroyAllWindows()
cap.release()