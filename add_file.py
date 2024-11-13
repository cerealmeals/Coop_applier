import pickle
import shutil
import os
import heapq

#functions for adding resumes and cover letters to bank of files

def add_cover_letter(file_path, priority, keyword):

    # make sure path is a docx
    if file_path[-5:] != '.docx':
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
        print('That keyword is already being used, the file for the keyword and priority is being updated')
    shutil.copy2(file_path, cover) # copy file to cover_letters folder

    obj = []
    prio = os.path.join(current, 'priority')
    # get priority file
    # if it doesn't exsits skip
    if os.path.exists(prio):
        try:
            f = open(prio, 'rb')
            obj = pickle.load(f)
            f.close()
        except Exception as e:
            print('Cover file load Error:',str(e))

    # put new keyword and priority into file
    heapq.heappush(obj, (-priority, keyword)) # negative priority because it is a min heap
    print(obj)

    # save file
    try:
        f = open(prio, 'wb+')
        obj = pickle.dump(obj, f)
        f.close()
    except Exception as e:
        print('Cover file dump Error:',str(e))

    return


def add_resume_letter(file_path, priority, keyword):

    # make sure path is a docx
    if file_path[-4:] != '.pdf':
        print('Rsumes need to the pdf format, just for simplity')
        return

    # create directory
    current = os.path.dirname(os.path.abspath(__file__))
    current = os.path.join(current, 'resumes')
    if not os.path.exists(current):
        os.makedirs(current)

    # copy file from path to new folder named the keyword
    cover = os.path.join(current, keyword + '.pdf')
    if os.path.exists(cover):
        print('That Resume is already being used, the file for the keyword and priority is being updated ')
    shutil.copy2(file_path, cover) # copy file to cover_letters folder

    obj = []
    prio = os.path.join(current, 'priority')
    # get priority file
    # if it doesn't exsits skip
    if os.path.exists(prio):
        try:
            f = open(prio, 'rb')
            obj = pickle.load(f)
            f.close()
        except Exception as e:
            print('Resume file load Error:',str(e))  

    # put new keyword and priority into file
    heapq.heappush(obj, (-priority, keyword)) # negative priority because it is a min heap

    print(obj)

    # save file
    try:
        f = open(prio, 'wb+')
        obj = pickle.dump(obj, f)
        f.close()
    except Exception as e:
        print('Resume file dump Error:',str(e))

    return
