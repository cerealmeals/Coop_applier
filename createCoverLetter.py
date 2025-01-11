from docx import Document # dependency
from docx2pdf import convert # dependency
from datetime import datetime
import os

current = os.path.dirname(os.path.abspath(__file__))
jobs = os.path.join(current, 'Jobs')


def createCoverLetter(title, file_name):

    # get your document using python-docx
    cover = os.path.join('cover_letters', file_name)
    doc = Document(cover)

    # get current date
    date = datetime.now()

    # replace word is a dict of symboles : word. Symboles are in the docx and word is gotten the the job page
    replace_word = {'[Date]': date.strftime("%B %e, %Y")}
    add, flag = read_file(title)
    replace_word.update(add)

    # walk through the cover letter replacing words
    for word in replace_word:
        for p in doc.paragraphs:
            if p.text.find(word) >= 0:
                p.text = p.text.replace(word, replace_word[word])

    # get the path to save the new docx
    save_path = os.path.join('cover_letters', title +'.docx')
    doc.save(save_path)
    
    # convert the docx to pdf
    convert(save_path)
    return flag

def read_file(file):

    result = {}
    try:
        f_jobs = open(os.path.join(jobs, file), 'r+')
        data = f_jobs.read()
        f_jobs.close()
    except Exception as e:
        print('file Error trying to read data', str(e))

    #temp = getLine(data, '#\nAddress Line One: ', '[Address]')
    result.update(getLine(data, '#\nAddress Line One: ', '[Address]') or '')
    result.update(getLine(data, '#\nCity: ', '[City]') or '')
    result.update(getLine(data, '#\nProvince / State: ', '[Province]') or '') # need to translate to letters
    result.update(getLine(data, '#\nPostal Code / Zip Code: ', '[Postal]') or '')
    result.update({'[Title]': file})
    result.update(getLine(data, '#\nOrganization: ', '[Company]') or '')

    start = data.find('Additional Application Information:')
    flag = False
    if start > -1:
        flag = True
        start += len('Additional Application Information:')
        end = data.find('#', start)
        string = data[start:end]
        todo = os.path.join(current, 'TODO')
        if not os.path.exists(todo):
            os.makedirs(todo)
        try:
            todo = os.path.join(todo, file)
            os.makedirs(todo)
            f = open(os.path.join(todo, file), 'w+')
            f.write(string)
            f.close()
        except Exception as e:
            print('file Error trying to read data', str(e))
    
    return result, flag
    

def getLine(data, line, type):
    start = data.find(line)
    if start > -1:
        start += len(line)
        end = data.find('#', start)
        string = data[start:end]
        return {type:string}
    return