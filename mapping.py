def mapExtention(extention):	
	index = 0
	try:
		index = dict[extention]
	except KeyError:
		index = 11

	return(list[index])



folderPath = '/Users/shishir/Desktop/folder/'
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

dict = {
	'.ai' :0,
	'.psd' : 0,
	'.c' : 1,
	'.cpp' : 1,
	'.dmg' : 2,
	'.docx' : 3,
	'.txt' : 3,
	'.tex' : 3,
	'.pages' : 3,
	'.numbers' : 3,
	'.ppt' : 3,
	'.pptx' : 3,
	'.xls' : 3,
	'.xlsx' : 3,
	'.html' : 4,
	'.css' : 4,
	'.png' : 5,
	'.jpg' : 5,
	'.jpeg' : 5,
	'.pdf' : 6,
	'.py' : 7,
	'.torrent' : 8,
	'.mp4' : 9,
	'.mkv' : 9,
	'.zip' : 10,
}


list = [ai_folder, c_folder, dmg_folder, documents_folder, html_folder, images_Folder, pdf_folder, python_folder, torrent_folder, videos_folder, zip_folder, others_folder]


