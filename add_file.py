import pickle
import shutil
import os

#functions for adding resumes and cover letters to bank of files

def add_cover_letter(file_path, priority, keyword):

    # make sure path is a docx
    if file_path[-5:-1] != '.docx':
        print('Cover letters templates need to the docx format, they will be converted to pdf before being uploaded')
        return

    # create directory
    current = os.path.dirname(os.path.abspath(__file__))
    current = os.path.join(current, 'cover_letters')
    if not os.path.exists(current):
        os.makedirs(current)

    # copy file from path to new folder named the keyword
    cover = os.path.join(current, keyword + '.docx')
    if os.path.exists(cover):
        print('That keyword is already being used, the file for the keyword is being updated')
    shutil.copy2(file_path, cover) # copy file to cover_letters folder

    obj = []
    prio = os.path.join(current, 'priorty')
    # get priority file
    # if it doesn't exsits skip
    if os.path.exists(prio):
        try:
            f = open(prio, 'rb')
            obj = pickle.load(f)
            f.close()
        except Exception as e:
            print('file Error',str(e))  

    # put new keyword and priority into file
    obj.append((priority, keyword)) # make this acutally a priority queue


    # save file
    

    

    
    
    # update priority file


    return


def add_resume_letter(path, priority, keyword):
    return