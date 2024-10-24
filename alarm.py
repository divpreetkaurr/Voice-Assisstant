import pyttsx3
import datetime
import os

# Initialize the speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
extractedtime = open("alarmtext.txt","rt")
time= extractedtime.read()

Time= str(time)
extractedtime.close()

deletetime = open("alarmtext.txt","r+")
deletetime.truncate(0)
deletetime.close()

def ring(time):
    timeset = str(time)
    timenow= timeset.replace("bestie", "")
    timenow=timenow.replace("set an alarm","")
    timenow=timenow.replace(" and ",":")
    AlarmTime= str(timenow)
    print(AlarmTime)
    while True:
        currenttime= datetime.datetime.now.strftime("%H:%M:%S")
        if currenttime == AlarmTime:
            speak("Alarm ringing,Bestie")
            os.startfile("AUD-20241020-WA0001.dat")
        elif currenttime+"00:00:30"==AlarmTime:
            exit()
            
        
ring(time)