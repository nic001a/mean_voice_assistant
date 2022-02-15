from gtts import gTTS
from playsound import playsound

tts = gTTS(text="Hello motherfucker, I want to tell you that you have a very, very nice ass ", lang="en")
tts.save("hello.mp3")
playsound("hello.mp3")