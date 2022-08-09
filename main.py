import os
import urllib.request
import moviepy.video.io.VideoFileClip
import praw
from moviepy.editor import CompositeVideoClip
import textwrap
import shutil
from termcolor import colored


videos = int(input('How many Images do you want:  '))
count = 0
video = moviepy.editor.VideoFileClip('Background video/bg_video.mp4')
reddit = praw.Reddit(client_id='YourClientID', client_secret='YourSecret', user_agent='Python', username='Yourusername',)
subreddit = reddit.subreddit("MapPorn")
Text3 = False
Text4 = False
destination = 'D:\Reddit Videos'
Error = 0
LogoError = 0
IndexError = 0
ErrnoError = 0



for submission in subreddit.new(limit=None):

    url = str(submission.url)
    title = submission.title
    parts = textwrap.wrap(title, 25)

    try:
        # Check if the link is an image
        if url.endswith("jpg") or url.endswith("jpeg") or url.endswith("png") or url.endswith("mp4") or url.endswith("mov") or url.endswith("wmv") or url.endswith("avi"):

            # Retrieve the image and save it in current folder
            Imagename = f"Images/image{count}.png"
            save = urllib.request.urlretrieve(url, Imagename)
            try:
                logo = (moviepy.editor.ImageClip(Imagename).set_duration(10).resize(height=550, width=420).set_pos('center'))
            except:
                Error += 1
                LogoError += 1
            txt1 = (moviepy.editor.TextClip(parts[0], fontsize=30, color='black'))
            txt1 = txt1.set_position((10, 15)).set_duration(10)


            if len(title) > 25:
                try:
                    Text2 = True
                    txt2 = (moviepy.editor.TextClip(parts[1], fontsize=30, color='black'))
                    txt2 = txt2.set_position((10, 40)).set_duration(10)
                except:
                    Error += 1
                    IndexError += 1
                    print(colored('IndexError', 'green'))

                if len(title) > 50:
                    try:
                        Text3 = True
                        txt3 = (moviepy.editor.TextClip(parts[2], fontsize=30, color='black'))
                        txt3 = txt3.set_position((10, 70)).set_duration(10)
                    except:
                        Error += 1
                        IndexError += 1
                        print(colored('IndexError', 'green'))
                    if len(title) > 75:
                        try:
                            Text4 = True
                            txt4 = (moviepy.editor.TextClip(parts[3], fontsize=30, color='black'))
                            txt4 = txt4.set_position((10, 100)).set_duration(10)
                        except:
                            Error += 1
                            IndexError += 1
                            print(colored('IndexError', 'green'))

                if Text3 == True:
                    if Text4 == True:
                        final_video = moviepy.editor.CompositeVideoClip([video, logo, txt1, txt2, txt3, txt4])
                    else: final_video = moviepy.editor.CompositeVideoClip([video, logo, txt1, txt2, txt3])
                else:

                    final_video = moviepy.editor.CompositeVideoClip([video, logo, txt1, txt2,])
            else:
                final_video = moviepy.editor.CompositeVideoClip([video, logo, txt1], method='compose')
            try:
                video_name = f'{count, title}test.mp4'
                final_video.write_videofile(video_name, fps=60, codec="h264_nvenc")
            except IOError:
                print('Errno32')
                ErrnoError += 1
                Error += 1


            print('This is number :', count)
            count += 1

            try:
                shutil.move(video_name, destination)
                print(video_name + " was moved")
            except :
                print(video_name + " was not found")
            if count == videos:
                succesful = videos - Error
                print(colored(f'{succesful}videos', 'red'))
                break
    except:
        Error +=1

os.system('concatenate.py 1')