import moviepy.editor as moviepy
import os.path as op

def extract_mp3(video, audio):
    if (video == audio):
        print("ERROR: source and destination file are the same")
        exit() # TODO CHANGE THIS TO SOMETHING THAT DOESNT STOP RUNNING
    video = f"./backend/data/{video}"
    audio = f"./backend/data/{audio}"

    if (op.isfile(audio)):
        print("ERROR: destination file exists already!")

    else:
        clip = moviepy.VideoFileClip(video)
        clip.audio.write_audiofile(audio)

