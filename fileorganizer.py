from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time
import json

folderPath = '/Users/shishir/Desktop/folder/'

folder_to_track = folderPath 
ai_folder = folderPath + 'ai or PSD'
c_folder = folderPath + 'C or C++'
dmg_folder = folderPath + 'DMG'
documents_folder = folderPath + 'Documents'
html_folder = folderPath + 'HTML'
images_Folder = folderPath + 'Images'
pdf_folder = folderPath + 'PDF'
python_folder = folderPath + 'Python'
torrent_folder = folderPath + 'Torrent'
videos_folder = folderPath + 'Videos'
zip_folder = folderPath + 'Zip files'
others_folder = folderPath + 'Others'






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

	def checkExt(ext):
		ai = ['.ai','.psd']
		c = ['.c','.cpp']
		doc = ['.txt','.docx','pages']
		if ext in ai




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
