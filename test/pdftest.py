import PyPDF2

with open('hsdecmenu.pdf', 'rb') as pdfFileObj:
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    text = pageObj.extractText()

_3rd_day_menu = text[text.find('3'):text.find('7')]
print(_3rd_day_menu)