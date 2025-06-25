import os
import cv2
import numpy as np

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
    for i in range(h - 1, -1, -1):
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
    for i in range(w - 1, -1, -1):
        if np.std(gray[:, i]) < threshold:
            right += 1
        else:
            break
    return top, bottom, left, right

input_folder = 'input'
output_folder = 'output'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.png', '.jpeg')):
        path = os.path.join(input_folder, filename)
        image = cv2.imread(path)
        top, bottom, left, right = detect_border(image)
        h, w = image.shape[:2]
        cropped = image[top:h-bottom if bottom > 0 else h, left:w-right if right > 0 else w]
        out_path = os.path.join(output_folder, filename)
        cv2.imwrite(out_path, cropped)
        print(f'Cropped image saved: {out_path}')
