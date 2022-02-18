from gtts import gTTS
from playsound import playsound
import csv


def weather_response():
    tts = gTTS(
        text="help me please !!!", lang="en")
    tts.save("weather.mp3")
    playsound("weather.mp3")

# weather_response() will take respond according to a certain inpu
# it will write the response text output the audio and read the audio


def small_pp():
    tts = gTTS(
        text="Fuck you dumbass I am a super smart robot and I'll come for you", lang="en")
    tts.save("stupid.mp3")
    playsound("stupid.mp3")


def curse_response(word_here):
    with open('curse_eng.csv') as csv_file:
        file_read = csv.reader(csv_file)
        if word_here in csv_file:
            small_pp()

def subscribe():
    tts = gTTS(
    text="Before you leeave consider subscribing and supporting this project on patreon, Motherfucker ", lang="en")
    tts.save("sub.mp3")
    playsound("sub.mp3")

subscribe()