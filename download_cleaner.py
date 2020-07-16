import os
import time
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler
from file_utilities import *


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_created(event):
        if os.path.isdir(event.src_path):
            return
        for type_of_file in types_of_file.keys():
            if is_type_file(event, type_of_file):
                path_to_folder = make_folder(type_of_file)
                move_to_new_corresponding_folder(event, path_to_folder)
                return
    
    @staticmethod
    def on_modified(event):
        pass

    @staticmethod
    def on_deleted(event):
        pass

    @staticmethod
    def on_moved(event):
        pass


file_change_handler = Handler()
observer = Observer()
os.chdir(PATH_OF_FOLDER)
print(os.getcwd())
observer.schedule(file_change_handler, os.getcwd(), recursive=False,)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()