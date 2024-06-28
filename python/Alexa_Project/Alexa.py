import speech_recognition as sr
import webbrowser
import gtts
import os 
import playsound
import time

class VoiceAssistant:

    def text_to_speech(self, speech: str):
        filename = "audiofile.mp3"
        tts = gtts.gTTS(speech)
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)
        return 


    def speech_to_text(self):
        text = ""
        speech = sr.Recognizer()
        with sr.Microphone() as micophone:
            print("start speaking")
            speech.adjust_for_ambient_noise(micophone)
            audio=speech.listen(micophone)

        try:
            text = speech.recognize_google(audio)
            print("thinks you said " + text)
        except sr.UnknownValueError:
            print(" could not understand audio")
        except sr.RequestError as e:
            print(" error; {0}".format(e))
        return text
    def excute_action(self,data :str):

        
        if ("google" in data):
            self.text_to_speech("okey")
            webbrowser.open('https://www.google.com/')
            self.text_to_speech("you can use it now")

        if ("facebook" in data):
            self.text_to_speech("okey")
            webbrowser.open("https://www.facebook.com/")
            self.text_to_speech("you can use it now")

        elif ("youtube" in data):
            self.text_to_speech("okey")
            webbrowser.open('https://www.youtube.com/')
            self.text_to_speech("you can use it now")
        elif ("time" in data):

            self.text_to_speech("time now is " + time.ctime())

        elif ("code" in data):
            os.system("code &")

        else:
            raise Exception("option not supported")   

voiceAssistant =VoiceAssistant()
voiceAssistant.text_to_speech("Hi How can i help you")
while True:
    try:
        data = voiceAssistant.speech_to_text().lower()
        voiceAssistant.excute_action(data)
        break

    except Exception:
        voiceAssistant.text_to_speech("option not supported please choose another option")

