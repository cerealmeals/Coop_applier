from python_docx_replace import docx_replace
from docx import Document
import datetime
import os

current = os.getcwd()
current = os.path.join(current, 'Jobs')

def createCoverLetter(file):

    data = read_file(file)
    # # get your document using python-docx
    doc = Document("Cover_letter_test.docx")

    date = datetime.datetime.now()
    replace_word = {'[Date]': date.strftime("%B %b, %Y"), '[Company]': 'ABC'}

    for word in replace_word:
        for p in doc.paragraphs:
            if p.text.find(word) >= 0:
                p.text = p.text.replace(word, replace_word[word])

    
    
    doc.save(file + ".docx")

def read_file(file):

    try:
        f = open(os.path.join(current, file), 'r+')
        data = f.read()
    except Exception as e:
        print('file Error trying to read data', str(e))

    Company_start = '#\nAddress Line One: '.find()


createCoverLetter('123757 - Software Developer')