import pyttsx3 as pt
from PyPDF2 import PdfReader
from pygame import mixer
def stop():
    mixer.music.stop()
def pause():
    mixer.music.pause()
def unpause():
    mixer.music.unpause()

book = open("EnglishBook.pdf", "rb")
pdfReader = PdfReader(book)
pages = len(pdfReader.pages)
print(pages)
bot=pt.init()
voice = bot.getProperty('voices')
bot.setProperty('voice', voice[1].id)
for num in range(8,pages):
    page = pdfReader.pages[8]
    text = page.extract_text()
    bot.say(text)
    bot.runAndWait()



