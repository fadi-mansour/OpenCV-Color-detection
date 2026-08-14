import argparse
import cv2
import pandas as pd
import numpy as np # FIX 2: Added numpy import

# 1. Argument parsing and image loading
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['image']
img = cv2.imread(img_path)
original_img = img.copy()

# 2. Read the CSV
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

# FIX 4: Initialize global variables BEFORE using them
clicked = False
r = g = b = xpos = ypos = 0

# 3. Define the functions 
def draw_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, xpos, ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

def getColorName(R, G, B):
    target_color = np.array([R, G, B])
    dataset_colors = csv[['R', 'G', 'B']].values
    distances = np.abs(dataset_colors - target_color).sum(axis=1)
    min_index = distances.argmin()
    return csv.loc[min_index, "color_name"]

# 4. Set up the window and attach the callback LAST
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

# 5. Display loop
while(1):
    cv2.imshow("image", img)
    if (clicked):
        img = original_img.copy()
        cv2.rectangle(img, (xpos,ypos), (xpos+750,ypos+60), (b,g,r), -1)
        text = getColorName(r,g,b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
        cv2.putText(img, text, (xpos+10,ypos+30), 2, 0.8, (255,255,255), 2, cv2.LINE_AA)
        
        if (r+g+b >= 600):
            cv2.putText(img, text, (xpos+10,ypos+30), 2, 0.8, (0,0,0), 2, cv2.LINE_AA)
            
        clicked = False

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()