import os
import assemblyai as aai
from .src.transformer import summarize_text





APIKEY = "b7bf577d488b4a0084395568209f526b"
def STT(file):
    audio = file


    aai.settings.api_key = APIKEY
    transcriber = aai.Transcriber()


    transcript = transcriber.transcribe(f"backend/data/{file}.wav")

    # transcript = transcriber.transcribe("./my-local-audio-file.wav")
    lista = []
    with open(f"./backend/data/text{audio}.txt", "w") as file:
        for line in transcript.text:
            file.write(line)
            lista.append(line)
    print("FILE >TXT CREATED > > >")
    return "".join(lista)

def summarize(audio):
    audio = audio.split('/')[-1][0:-4]
    stringa = STT(audio)
    summarize_text(stringa)


