from gtts import gTTS
import os
tts = gTTS(text='bon nuit', lang='fr')
tts.save("good.mp3")
os.system("cvlc good.mp3")
