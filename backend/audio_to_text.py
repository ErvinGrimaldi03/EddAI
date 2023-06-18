# `pip3 install assemblyai` (macOS)
# `pip install assemblyai` (Windows)

import assemblyai as aai
audio = 'test'

APIKEY = "b7bf577d488b4a0084395568209f526b"
aai.settings.api_key = APIKEY
transcriber = aai.Transcriber()

transcript = transcriber.transcribe("./data/test.wav")
# transcript = transcriber.transcribe("./my-local-audio-file.wav")

with open(f"./data/text{audio}.txt", "w") as file:
    for line in transcript.text:
        file.write(line)