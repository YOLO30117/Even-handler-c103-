import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/Lolo/Downloads"              # Add the path of you "Downloads" folder.
to_dir = "Krish_Files" 

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}


class FileMovementHandler(FileSystemEventHandler):
    
     def on_created(self, event):
          name,ext = os.path.splitext(event.src_path)
          time.sleep(1)
          for key,value in dir_tree.items():
               time.sleep(1)
               if ext in value:
                 fname = os.path.basename(event.src_path)
                 print("Downloaded " + fname)
                 p1 = from_dir + "/" + fname
                 p2 = to_dir + "/" + key
                 p3 = to_dir + "/" + key + "/" + fname
            
               if os.path.exists(p2):
                 print("Moving " + fname + ".....")
                 shutil.copy(p1,p3)
                 time.sleep(1)
               else:
                 os.makedirs(p2)  
                 print("Moving " + fname + ".....")
                 shutil.copy(p1,p3)  
                 time.sleep(1)



evt_h = FileMovementHandler()

ob = Observer()
ob.schedule(evt_h,from_dir,recursive=True)
ob.start()

try:
    while True:
        time.sleep(2)
        print('running')
except KeyboardInterrupt:
     print("stopped!")
     ob.stop()