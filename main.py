import threading
from frontend import camera_prompt
def run():
    print("To quit recording. Press 'q': ")
    camera_prompt.camera()



if __name__ == "__main__":
    run()