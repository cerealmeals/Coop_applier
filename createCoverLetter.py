from docx import Document
from docx2pdf import convert
import datetime
import os

current = os.getcwd()
jobs = os.path.join(current, 'Jobs')


def createCoverLetter(file):

    data = read_file(file)
    # # get your document using python-docx
    cover = os.path.join('cover_letters', "Cover_letter_test.docx")
    doc = Document(cover)

    date = datetime.datetime.now()
    replace_word = {'[Date]': date.strftime("%B %b, %Y")}
    replace_word.update(read_file(file))

    for word in replace_word:
        for p in doc.paragraphs:
            if p.text.find(word) >= 0:
                p.text = p.text.replace(word, replace_word[word])

    
    save_path = os.path.join('cover_letters', file +'.docx')
    doc.save(save_path)
    convert(save_path)

def read_file(file):

    result = {}
    try:
        f_jobs = open(os.path.join(jobs, file), 'r+')
        data = f_jobs.read()
    except Exception as e:
        print('file Error trying to read data', str(e))


    result.update(getLine(data, '#\nAddress Line One: ', '[Address]'))
    result.update(getLine(data, '#\nCity: ', '[City]'))
    result.update(getLine(data, '#\nProvince / State: ', '[Province]')) # need to translate to letters
    result.update(getLine(data, '#\nPostal Code / Zip Code: ', '[Postal]'))
    result.update({'[Title]': file})
    result.update(getLine(data, '#\nOrganization: ', '[Company]'))

    
    
    return result
    

def getLine(data, line, type):
    start = data.find(line)
    if start > -1:
        start += len(line)
        end = data.find('#', start)
        string = data[start:end]
        return {type:string}
    return


createCoverLetter('123757 - Software Developer')