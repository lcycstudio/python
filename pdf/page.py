from PyPDF2 import PdfReader
import io

page_size_dict = {
    'LETTER': {
        'pointsPerInch': 72,
        'width': 8.5,
        'height': 11,
        'validationErrorMsg': 'Document must be set to fit onto 8.5” x 11” letter-size paper'
    }
}

with open('badPDF.pdf', 'rb') as f:
    contents = f.read()

open_pdf_file = io.BytesIO(contents)
reader = PdfReader(open_pdf_file)
page_nums = reader.getNumPages()
is_valid_page_size = True
for page_num in range(page_nums):
    x, y, w, h = reader.pages[1].mediabox
    width = w - x
    height = h - y
    page_size_info = page_size_dict.get('LETTER')
    is_valid_page_size = width / page_size_info.get('pointsPerInch') == page_size_info.get('width') and \
                        height / page_size_info.get('pointsPerInch') == page_size_info.get('height')
    if not is_valid_page_size: break

print('is_valid_page_size: ', is_valid_page_size)

#       isvalidPageSize = (width / pageSizeInfo.pointsPerInch === pageSizeInfo.width) &&
#         (height / pageSizeInfo.pointsPerInch === pageSizeInfo.height)

# print('page_nums: ', page_nums)
# print(reader.pages[0].mediabox[0])
