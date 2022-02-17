import speech_recognition as sr
import txttospch
import csv_reader

r = sr.Recognizer()
with sr.Microphone() as source:
    r.pause_threshold = 1
    r.adjust_for_ambient_noise(source)
    print("Listening...")
    audio = r.listen(source)
try:
    print("Recognizing...")
    query = r.recognize_google(audio, language='en-in')
    print(f"user said: {query}\n")

    if 'weather' in query:
        txttospch.weather_response()
    
  

    txttospch.curse_response(query)
   #this is not working curse rspns 
except Exception as e:
    print("BRO STFU")
