import cv2
import pytesseract
from tqdm import tqdm

# Set the path to the Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = r'./tesseract-5.3.0-x86_64.AppImage'

# Set the video paths
input_video_path = './Data/test2.mp4'
output_video_path = './result.mp4'

# Initialize the video capture
video_capture = cv2.VideoCapture(input_video_path)
fps = video_capture.get(cv2.CAP_PROP_FPS)
width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
length = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))

# Initialize the video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

for cur_frame_no in tqdm(range(int(length/10))):
    # Read the next frame from the video
    video_capture.set(cv2.CAP_PROP_POS_FRAMES, cur_frame_no)
    ret, frame = video_capture.read()
    if not ret:
        break

    # Perform OCR on the frame
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Write the modified frame to the output video
    video_writer.write(frame)

# Release the video capture and writer
video_capture.release()
video_writer.release()
