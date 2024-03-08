import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
fromdir='C:/Users/dell/Downloads'
todir='C:/Users/dell/Desktop/Download_files'
dir_tree={
    'image_files':['.jpg','.png','.jfif','.gif'],
    'video_files':['.mp4','.mpg','.mp2','.mpv','.avi','.mov'],
    'documant_files':['.pdf','.py','.html','.ppt','.txt','.xls'],
    'setup_files':['.exe','.cmd','.bin','.msi','.dmg']
    }
class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
        root.ext=os.path.splitext(event.sourcePath)
        time.sleep(1)
        for key,value in dir_tree.items():
            time.sleep(1)
            if ext in value:
                fileName=os.path.basename(event.sourcePath)
                path1=fromdir+'/'+fileName
                path2=todir+'/'+key
                path3=todir+'/'+key+'/'+fileName
                if os.path.exists(path2):
                    shutil.move(path1,path3)
                    time.sleep(1)
                else:
                    os.mkdir(path2)
                    shutil.move(path1,path3)
                    time.sleep(1)
eventHandler=FileMovementHandler()
observer=Observer()
oberserver.schedule(eventHandler,fromdir,recursive=True)
observer.start()
try:
    while True:
        time.sleep(2)
        print('running')
except KeyboardInterrupt:
    print('stopped')
    observer.stop()
           
