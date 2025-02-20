from PyPDF2 import PdfWriter
import os

merger = PdfWriter()

for file in os.listdir("./documents/"):
    if file.endswith(".pdf"):
        merger.append(file)
    merger.write("merged.pdf")





