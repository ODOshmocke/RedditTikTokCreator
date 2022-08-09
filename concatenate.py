from moviepy.editor import concatenate_videoclips
from moviepy.video.io.VideoFileClip import VideoFileClip
import os
import time


def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]
path = listdir_fullpath('D:\Reddit Videos')
print(path)
files_list = [ fname for fname in path if fname.endswith('.mp4')]
print(files_list)

clips = [VideoFileClip(c) for c in files_list]
start_time = time.time()
final_video = concatenate_videoclips(clips, method='compose')
final_video.write_videofile('video.mp4', fps=60, threads=16, codec="libx264")
print(str(time.time() - start_time), 's')
#h264_nvenc, 251.9737548828125 s
#libx264, 274.2242240905762 s




