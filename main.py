import threading
from frontend import camera_prompt
from backend import convert_to_audio
from backend import audio_to_text
from backend import questions

def run():
    print("To quit recording. Press 'q': ")

    camera_prompt.camera()
    convert_to_audio.extract_mp3("lecture.mp4", "lecture_audio.wav")
    sommario = audio_to_text.summarize("lecture_audio.wov")
    from backend import humeApi
    humeApi.get_request("./data/camera_video.mp4")

    print("""++++MENU++++
             1: Practice Quiz
             2: Class Notes
             3: Quit""")
    choice = input("Input:")
    while (choice != 3):
        if (choice == 1):
            print("Preparing Quiz. . .")
            questions.retrive_quiz()
        elif (choice == 2):
            print("Preparing Notes. . .")
            questions.retrive_Notes()
        elif (choice == 3):
            print("Bye!")
            quit()
        else:
            print("invalid input")
        choice = input("Input:")





if __name__ == "__main__":
    run()