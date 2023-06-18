import os
import openai

def get_summ():
    file_path = "./data/summary.txt"
    file = open(file_path, 'r')
    summary = file.read()
    file.close()
    summary += " WHAT IS THE TOPIC? GIVE ANSWER ONLY, NO OTHER WORDS BESIDES THE ANSWER"
    return summary
def retriveTopic():

    openai.api_key = "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"

    propy = get_summ()
    start_sequence = "\nAI:"
    restart_sequence = "\nHuman: "

    response = openai.Completion.create(
      model="text-davinci-003",
      prompt= propy,
      temperature=0.9,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.6,
      stop=[" Human:", " AI:"])

    return response['choices'][0]['text']


def retrive_quiz():
    openai.api_key = "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"

    topicy = retriveTopic()
    start_sequence = "\nAI:"
    restart_sequence = "\nHuman: "

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="The topic is " + topicy + " Generate 3 multiple choice questions about the topic. Don't be common, and don't give answers ",
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"])

    return response['choices'][0]['text']

def retrive_Notes():
    openai.api_key = "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"

    topicy = retriveTopic()
    start_sequence = "\nAI:"
    restart_sequence = "\nHuman: "

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="The topic is " + topicy + " Generate notes about the topic that could be useful to a college student. Be technical when possible",
        temperature=0.9,
        max_tokens=350,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"])

    return response['choices'][0]['text']
