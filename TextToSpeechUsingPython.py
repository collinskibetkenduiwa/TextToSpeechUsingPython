#install gtts using pip
from gtts import gTTS
import os

MyText="Text To Speech Using Python"

#opening a file
fh= open("Texttest.txt",'r')
my_text=fh.read().replace('/n',' ')

language='en'

output=gTTS(text=MyText,lang=language,slow=False)
 
output.save("Output.mp3")
fh.close()

os.system("start output.mp3")
