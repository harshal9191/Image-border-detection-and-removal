import csv
import numpy as np
import os
import cv2
import pandas as pd

input_folder = 'input'
output_csv = 'border_data.csv'

def detect_border(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    h, w = gray.shape
    threshold = 5
    top = 0
    for i in range(h):
        if np.std(gray[i, :]) < threshold:
            top += 1
        else:
            break
    bottom = 0
    for i in range(h -1,-1,-1):
        if np.std(gray[i, :]) < threshold:
            bottom += 1
        else:
            break
    left = 0
    for i in range(w):
        if np.std(gray[:, i]) < threshold:
            left += 1
        else:
            break
    right = 0
    for i in range(w -1,-1,-1):
        if np.std(gray[:, i]) < threshold:
            right += 1
        else:
            break
    return top, bottom, left, right

results = []
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg','.png','.jpeg')):
        path = os.path.join(input_folder, filename)
        image = cv2.imread(path)

        top, bottom, left, right = detect_border(image)

        results.append({
            'Image name' : filename,
            'Top': top,
            'Bottom': bottom,
            'Left': left,
            'Right':right,
            'width': left + right,
            'height': top + bottom
        })

# save these results to the csv file 
save_path = pd.DataFrame(results)
save_path.to_csv(output_csv, index=False)
print(f"report is created --->", output_csv)

