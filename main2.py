import pyttsx3
import PyPDF2
book = open('the_cooks_wedding_and_other_stories._the_tales_of_chekhov_xii.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

speaker = pyttsx3.init()
for num in range(1,140):
    page = pdfReader.getPage(1)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()