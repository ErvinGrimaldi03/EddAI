import requests

url = "https://api.hume.ai/v0/batch/jobs"
def reques_post(file):
    files = {"file": ("camera_video.mp4", open("./data/camera_video.mp4", "rb"), "video/mp4")}
    payload = {"json": "{}"}
    headers = {
        "accept": "application/json",
        "X-Hume-Api-Key": "loUmzY9D2mxqbAk8y3LQliecybDvuKYG43RRZDq0KkNXBJXB"
    }

    response = requests.post(url, data=payload, files=files, headers=headers)
    get_request(response["job_id"])




def get_request(id):
    url = "https://api.hume.ai/v0/batch/jobs/0cf41b41-edee-482c-b486-106f8e5acbd2/predictions"

    headers = {
        "accept": "application/json; charset=utf-8",
        "X-Hume-Api-Key": "loUmzY9D2mxqbAk8y3LQliecybDvuKYG43RRZDq0KkNXBJXB"
    }

    response = requests.get(url, headers=headers)

    return response