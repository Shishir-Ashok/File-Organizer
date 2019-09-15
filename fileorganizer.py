from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time
import json


folder_to_track = '/Users/shishir/Desktop/folder' 
ai_folder = '/Users/shishir/Desktop/folder/ai or PSD'
c_folder = '/Users/shishir/Desktop/folder/C or C++'
dmg_folder = '/Users/shishir/Desktop/folder/DMG'
documents_folder = '/Users/shishir/Desktop/folder/Documents'
html_folder = '/Users/shishir/Desktop/folder/HTML'
images_Folder = '/Users/shishir/Desktop/folder/Images'
pdf_folder = '/Users/shishir/Desktop/folder/PDF'
python_folder = '/Users/shishir/Desktop/folder/Python'
torrent_folder = '/Users/shishir/Desktop/folder/Torrent'
videos_folder = '/Users/shishir/Desktop/folder/Videos'
zip_folder = '/Users/shishir/Desktop/folder/Zip files'
others_folder = '/Users/shishir/Desktop/folder/Others'






class MyHandler(FileSystemEventHandler):
	i =1
	# print("inside class\n")
	def on_modified(self,event):
		# print("inside self")
		for file in os.listdir(folder_to_track):
			if os.path.isfile(folder_to_track+ "/" + file):
				name, ext = os.path.splitext(file)
				if (ext == '.html'):
					src = folder_to_track + "/" + file
					new_destination = html_folder + "/" + file
					os.rename(src,new_destination)
				elif (ext == '.txt'):
					src = folder_to_track + "/" + file
					new_destination = documents_folder + "/" + file
					os.rename(src,new_destination)
				elif (ext == '.ai'):
					src = folder_to_track + "/" + file
					new_destination = ai_folder + "/" + file
					os.rename(src,new_destination)
				else:
					src = folder_to_track + "/" + file
					new_destination = others_folder + "/" + file
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
