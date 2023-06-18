import asyncio
import traceback

from utilities import download_file, print_emotions

from hume import HumeStreamClient
from hume.models.config import FaceConfig

filepath = download_file("https://storage.googleapis.com/hume-test-data/image/obama.png")


async def main():
    try:
        client = HumeStreamClient("loUmzY9D2mxqbAk8y3LQliecybDvuKYG43RRZDq0KkNXBJXB")

        # Enable face identification to track unique faces over the streaming session
        config = FaceConfig(identify_faces=True)
        async with client.connect([config]) as socket:
            result = await socket.send_file(filepath)
            emotions = result["face"]["predictions"][0]["emotions"]
            print_emotions(emotions)
    except Exception:
        print(traceback.format_exc())


# When running the streaming API outside of a Jupyter notebook you do not need these lines.
# Jupyter has its own async event loop, so this merges main into the Jupyter event loop.
# To run this sample in a script with asyncio you can use `asyncio.run(main())`
asyncio.run(main())
