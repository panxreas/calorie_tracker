import tabula, re
from pdfminer.high_level import extract_pages, extract_text

text = extract_text("./pdf/Equi.pdf")
listed = text.split('\n')
new_text = ''
for i in listed[6:]:
    if i == '':
        continue
    spaceless = i.split()
    new_text += ''


if __name__ == '__main__':
    print(listed[6:])
