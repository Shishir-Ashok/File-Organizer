from watchdog.observers import Observer
import time
import os
import json
from watchdog.events import PatternMatchingEventHandler



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
# filename = 'COnference paper.tex'
# src = folder_to_track + '/' + filename
# dest = folder_destination + '/' + filename

# os.rename(src,dest)

patterns = "*"
ignore_patterns = ""
ignore_directories = True
case_sensitive = True
event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

def on_change(event):
	for file in os.listdir(folder_to_track):
		if os.path.isfile(folder_to_track+ "/" + file):
			print(file)
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


event_handler.on_created = on_change
event_handler.on_deleted = on_change
event_handler.on_modified = on_change
event_handler.on_moved = on_change


go_recursively = True
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=go_recursively)
observer.start()


try:
	while True:
		time.sleep(10)
except KeyboardInterrupt:
	observer.stop()
observer.join()