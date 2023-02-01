# import PyPDF2
# reader = PyPDF2.PdfReader('UpperInt-Advanced_AnswerKey.pdf')
# # a= PyPDF2.PdfFileReader('uak.pdf')
# # print(a.documentInfo)
# print(reader)
from PyPDF2 import PdfReader

# reader = PdfReader("python exp\pdf operations using python\UpperInt-Advanced_AnswerKey.pdf")
page = reader.pages[0]
print(page.extract_text())