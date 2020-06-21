import re
import PyPDF2  

pdfFileObj = open('file.pdf', 'rb')  

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)  

for i in range(0,pdfReader.numPages):
    pageObj = pdfReader.getPage(i)
    text = pageObj.extractText()
    print(text)
    
pdfFileObj.close()  

text = re.sub(r'\[[0-9]*\]',' ',text)
text = re.sub(r'\s+',' ',text)
text = text.lower()
text = re.sub(r'\d',' ',text)
text = re.sub(r'\s+',' ',text)

def text():
    sentences = text