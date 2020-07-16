import shutil 
import os

PATH_OF_FOLDER = '/Users/vilelf/Downloads'

types_of_file = {
    'text': ('txt',),
    'pdf': ('pdf', 'mobi',),
    'mp3': ('mp3',),
    'image': ('png','jpg', 'jpeg', 'bmp','gif','raw'),
    'video': ('mov','mp4','avi','flv'),
    'doc': ('doc','docx'),
    'spreadsheet': ('xls','xlsx', 'csv'),
    'presentation': ('ppt','pptx'),
    'code': ('py','cs','js','php','html','sql','css','log','sh'),
    'executable': ('exe','msi', 'zip', 'dmg', 'pkg')
}


def extension_type(event):
    return event.src_path[event.src_path.rindex('.') + 1:]


def is_type_file(event, type_of_file):
    return extension_type(event) in types_of_file[type_of_file]


def make_folder(foldername):
    os.chdir(PATH_OF_FOLDER)
    if os.path.exists(foldername) == True:
        print('Folder already exists, skipping creation')
        return os.getcwd() + os.sep + str(foldername)
    else:
        os.mkdir(str(foldername))
        return os.getcwd() + os.sep + str(foldername)

def move_to_new_corresponding_folder(event,path_to_new_folder):
    try:
        shutil.move(event.src_path,path_to_new_folder)
        print('moving file')
    except:
        print('File already existed in target folder')
        pass