from PyPDF2 import PdfMerger

pdfs = [
    'Introduction.pdf',
    'Parenting.pdf',
    'Child_Support.pdf',
    'Spousal_Support.pdf',
    'Property.pdf',
    'Debts.pdf',
    'Conclusion.pdf'
]

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("Separation_Agreement.pdf")
merger.close()