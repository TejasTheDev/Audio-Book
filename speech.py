# import pyttsx3
# import PyPDF2

# book = open('D:\projects\Audio Book\pytho.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(book)
# pages = pdfReader.numPages
# print("Total pages")
# print(pages)

# speaker = pyttsx3.init()
# for num in range(10, pages):
#     page = pdfReader.getPage(10)
#     text = page.extract_text()
#     speaker.say(text)
#     speaker.runAndWait()





import pyttsx3   
speaker = pyttsx3.init()
speaker.say("i thrust u")
speaker.runAndWait()