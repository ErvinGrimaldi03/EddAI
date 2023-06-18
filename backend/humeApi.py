import requests
import os


from backend.src.serializer import get_top_emotions

url = "https://api.hume.ai/v0/batch/jobs"
def reques_post(file):
    files = {"file": (f"{file}", open(f"./backend/data/{file}", "rb"), "video/mp4")}
    payload = {"json": "{}"}
    headers = {
        "accept": "application/json",
        "X-Hume-Api-Key": "loUmzY9D2mxqbAk8y3LQliecybDvuKYG43RRZDq0KkNXBJXB"
    }

    response = requests.post(url, data=payload, files=files, headers=headers)
    id = response.text.split(":")[-1][1:-2]
    return get_request(id)


def get_request(id):
    url = "https://api.hume.ai/v0/batch/jobs/0cf41b41-edee-482c-b486-106f8e5acbd2/predictions"

    headers = {
        "accept": "application/json; charset=utf-8",
        "X-Hume-Api-Key": "loUmzY9D2mxqbAk8y3LQliecybDvuKYG43RRZDq0KkNXBJXB"
    }

    response = requests.get(url, headers=headers)
    return response

data = reques_post("camera_video.mp4").text
emotion_res = []
top_emotions = get_top_emotions(data, top_n=5)
for emotion in top_emotions:
    print(f"{emotion['name']}: {emotion['score']}")
