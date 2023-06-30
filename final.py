import cv2
from tqdm import tqdm

def generate_output(input_path):
    vidcap = cv2.VideoCapture(input_path)
    length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame = 0

    for frame in tqdm(range(0, length)):
        vidcap.set(cv2.CAP_PROP_POS_FRAMES, frame)
        success, image = vidcap.read()
        if not success:
            break

## Parallel reading is needed for faster processing


if(__name__ == '__main__'):
    generate_output('./Data/test2.mp4')