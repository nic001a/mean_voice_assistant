from gtts import gTTS
from playsound import playsound
import csv


def weather_response():
    tts = gTTS(
        text="HUmanity has spent so many years developing internet machine learning and programming languages and the first you can think about is to ask about the weather ? stick your head out of the window and shut up!", lang="en")
    tts.save("weather.mp3")
    playsound("weather.mp3")

# weather_response() will take respond according to a certain inpu
# it will write the response text output the audio and read the audio


def small_pp():
    tts = gTTS(
        text="More real than you", lang="en")
    tts.save("stupid.mp3")
    playsound("stupid.mp3")


def curse_response(word_here):
    with open('curse_eng.csv') as csv_file:
        file_read = csv.reader(csv_file)
        if word_here in csv_file:
            small_pp()


def roast():
    tts = gTTS(
    text="Bob the builder took one look at you and said we cant fix that!", lang="en")
    tts.save("stupid.mp3")
    playsound("stupid.mp3")