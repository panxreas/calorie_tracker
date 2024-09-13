import tabula, re
import os

#from pdfminer.high_level import extract_pages, extract_text
#text = extract_text("./pdf/Equi.pdf")

folder_path = './'
file_name = 'equivalencias.txt'
file_path = os.path.join(folder_path, file_name)

#file = open(file_path, 'w')
#listed = file.write(text)
#file.close()

file = open(file_path, 'r')
listed = file.read()
file.close()

list_file = listed.split('\n')

def edit_txt(text):
    elements = text.rstrip().split("   ")
    if len(elements) <= 1:
        return (elements[0])
    food = elements[0].strip()
    quanty = elements[-1].strip()
    return (food, quanty)


clean = list(filter(lambda x: x != '' and not x.isspace(), list_file[6:]))
data = list(map(edit_txt, clean))

equivalencia = {}
categoria = None

for alimento in data:
    if isinstance(alimento, str):
        categoria = alimento
        equivalencia[categoria] = {}
        continue
    equivalencia[categoria][alimento[0]] = alimento[1]

if __name__ == '__main__':
    with open('./equivalencias.py', 'w') as file:
        file.write(f"equivalencia = {equivalencia!r}\n")
    print("Dictionary has been exported")
