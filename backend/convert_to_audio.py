import moviepy.editor as moviepy

def extract_mp3():
    clip = moviepy.VideoFileClip(r"./data/test.mp4")
    clip.audio.write_audiofile(r"./data/test.mp3")