import cv2

# Print the version information of OpenCV
print("OpenCV version:", cv2.__version__)

# Check if H.264 codec is supported
if cv2.getBuildInformation().find('H.264') != -1:
    print("H.264 codec is supported.")
else:
    print("H.264 codec is not supported.")
