#Speech to text program
#pip install SpeechRecognition

import speech_recognition as sr
def speech_to_text():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        audio=recognizer.listen(source)
    try:
        text=recognizer.recognize_google(audio)
        print("You said:",text)
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
speech_to_text()


# def audiofile_to_text():
#     mp3_file="output.mp3"
#     audio_file="output.wav"
#     recognizer=sr.Recognizer()
#     with sr.AudioFile(audio_file) as source:
#         print("Processing audio file...")
#         audio=recognizer.record(source)
#     try:
#         text=recognizer.recognize_google(audio, language='en-US')
#         print("The audio file contains:",text)
#         return text
#     except sr.UnknownValueError:
#         print("Sorry, could not understand the audio.")
#     except sr.RequestError as e:
#         print("Could not request results; {0}".format(e))
# audiofile_to_text()
