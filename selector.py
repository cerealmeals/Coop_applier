import os
import pickle

def selector(title):

    # find the file with priorities.
    current = os.path.dirname(os.path.abspath(__file__))
    current = os.path.join(current, 'cover_letters', 'priority')

    try:
        f = open(current, '+rb')
        obj = pickle.load(f)
        f.close()
    except Exception as e:
        print('Cover file load Error:',str(e))
    
    # format the title
    lower_case_title = title.lower()

    tup = None
    i = 0
    # walk through the keywords by priority
    while i < len(obj):
        tup = obj[i]
        if lower_case_title.find(tup[1].lower()) != -1:
            break
    
    # the highest priority keyword picks the cover letter
    cover_name = tup[1] + '.docx'
    resume_name = tup[1] + '.pdf'
    # return the file name of the cover letter template, and the resume name.
    return cover_name, resume_name
