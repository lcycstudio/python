from PIL import Image

from PyPDF2 import PdfMerger

# image_1 = Image.open('screenshot.png')
# im_1 = image_1.convert('RGB')
# im_1.save('new.pdf')

pdfs = [
    'new.pdf',
    'docu.pdf',
]

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("testFor.pdf")
merger.close()