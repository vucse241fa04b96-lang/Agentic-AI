#text to speech
#pip install gttS
from gtts import gTTS
def text_to_speech(text, lang='en'):
    speech=gTTS(text=text, lang=lang, slow=False)
    speech.save("output.mp3")
#pip install googletrans==4.0.0-rc1
from googletrans import Translator
def English_text_to_Telugu(text):
    translator=Translator()
    translation=translator.translate(text, src='en', dest='te')
    telugu_text=translation.text
    print("telugu_text",telugu_text)
    speech=gTTS(text=telugu_text,lang='te',slow=False)
    speech.save("telugu_output.mp3")
text=input("Enter the text  you want to convert to speech: ")
English_text_to_Telugu(text)
text_to_speech(text)