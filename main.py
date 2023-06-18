import threading
from frontend import camera_prompt
from backend import convert_to_audio
from backend import audio_to_text

def run():
    print("To quit recording. Press 'q': ")

    camera_prompt.camera()
    convert_to_audio.extract_mp3("lecture.mp4", "lecture_audio.wav")
    sommario = audio_to_text.summarize("lecture_audio.wov")
    from backend import humeApi
    humeApi.get_request("./data/camera_video.mp4")





if __name__ == "__main__":
    run()