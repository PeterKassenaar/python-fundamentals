# example on how to create a small Text-To-Speech (TTS) program.
# Based on https://www.codingem.com/python-text-to-speech/

from gtts import gTTS
import os

mytext = "Hallo, dit is een voorbeeld van Text To Speech. Het gaat geweldig met de spraak mogelijkheden."
audio = gTTS(text = mytext, lang="nl", slow=False)

audio.save("example-tts.mp3")
os.system("start example-tts.mp3")
