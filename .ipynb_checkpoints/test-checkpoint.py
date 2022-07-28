# importing the required packages
import pyautogui
import cv2
import numpy as np



"""
image = cv2.imread('gg1.png', )
image=np.array(image)
print('shape=', image.shape)
cv2.imshow("ImageA",image) # the title and path to image
cv2.waitKey(0) # Waits for the next key to be pressed
cv2.destroyAllWindows()
# cv2.imwrite("watchgray.png",image)
""" 



img = pyautogui.screenshot()
# Convert the screenshot to a numpy array
frame = np.array(img)
# 

# Convert it from BGR(Blue, Green, Red) to
# RGB(Red, Green, Blue)
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
# frame=frame.mean(axis=2)

#print('frame=\n', frame)
print('frame shape=', frame.shape)
# Write it to the output file
# out.write(frame)

scale_percent = 60 # percent of original size
width = int(frame.shape[1] * scale_percent / 100)
height = int(frame.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
print('Resized Dimensions : ',resized.shape)

cv2.imshow("Resized image", resized[:, :600])

# Optional: Display the recording screen
# cv2.imshow('Live A', frame)
# cv2.resizeWindow("Live Pop", 460, 270)
cv2.waitKey(0) # Waits for the next key to be pressed
cv2.destroyAllWindows()




'''
# Specify resolution
resolution = (1920, 1080)

# Specify video codec
codec = cv2.VideoWriter_fourcc(*"XVID")

# Specify name of Output file
filename = "Recording.avi"

# Specify frames rate. We can choose any
# value and experiment with it
fps = 2 # 60.0


# Creating a VideoWriter object
out = cv2.VideoWriter(filename, codec, fps, resolution)

# Create an Empty window
cv2.namedWindow("Live PopA", cv2.WINDOW_NORMAL)

# Resize this window
cv2.resizeWindow("Live Pop", 460, 270)

# while True:
for jdx, jv in enumerate(np.arange(0,6)):
    print('jdx=', jdx)
    # Take screenshot using PyAutoGUI
    img = pyautogui.screenshot()
    print('a')
    # Convert the screenshot to a numpy array
    frame = np.array(img)
    print('b')
    # Convert it from BGR(Blue, Green, Red) to
    # RGB(Red, Green, Blue)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #print('c')
    # Write it to the output file
    out.write(frame)

    # Optional: Display the recording screen
    cv2.imshow('Live D', frame)

    # Stop recording when we press 'q'
    #if cv2.waitKey(0) == ord('q'):
    #    break
    print('e0 jv=', jv)

# Release the Video writer
out.release()

# Destroy all windows
cv2.destroyAllWindows()
'''