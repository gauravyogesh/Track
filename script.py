import subprocess
import os
import time
import cv2 
import pandas as pd 
from datetime import datetime


# Set the initial time
start_time = time.perf_counter()

# Set the delay in seconds
delay = 60

df = pd.DataFrame({"Status":[True, False, False, False, False, False, False, False]})

df.to_csv('saved.csv', index= False)

subprocess.run("git add .", shell=True, stdout=subprocess.PIPE, text=True)
subprocess.run(f"git commit -m 'www'", shell=True, stdout=subprocess.PIPE, text=True)
subprocess.run(f"git push origin main", shell=True, stdout=subprocess.PIPE, text=True)

ind_loc = 0
total_len = max(df.index)

for i in range(1,total_len):

    time.sleep(30)

    df['Status'].iloc[i] = True
    df['Status'].iloc[i-1] = False

    df.to_csv('saved.csv', index= False)

    subprocess.run("git add .", shell=True, stdout=subprocess.PIPE, text=True)
    subprocess.run(f"git commit -m 'www'", shell=True, stdout=subprocess.PIPE, text=True)
    subprocess.run(f"git push origin main", shell=True, stdout=subprocess.PIPE, text=True)
