import os
import cv2
def resize(input_file_path, output_file_path, width, height):
    os.system("ffmpeg -i {input} -vf scale={width}:{height} {output}".format(input=input_file_path, width=width, height=height, output=output_file_path))

resize(input_file_path='video/crab2x2.mp4', output_file_path='output_resize.mp4', width=500, height=500)

    
    