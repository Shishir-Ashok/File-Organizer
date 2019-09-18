from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time
import json
import mapping


folder_to_track = '/Users/shishir/Desktop/folder/'
class MyHandler(FileSystemEventHandler):
	
	def on_modified(self,event):
		for file in os.listdir(folder_to_track):
			if os.path.isfile(folder_to_track+ "/" + file):
				name, ext = os.path.splitext(file)
				folderName = mapping.mapExtention(ext)
				src = folder_to_track + "/" + file
				new_destination = folderName + "/" + file
				os.rename(src,new_destination)

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler,folder_to_track,recursive=True)
observer.start()

try:
	while True:
		time.sleep(1)
except KeyboardInterrupt:
	observer.stop()
observer.join()
